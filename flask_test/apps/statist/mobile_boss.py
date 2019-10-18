# coding=utf-8
# @Time    : 2018/10/22 下午3:24
# @Author  : Zuyong Du
import datetime

from flask_restful import Resource, reqparse

from application import db
from apps.utils.res import json_response

from typing import (
    List,
    Dict,
    Any,
)

from apps.statist.enum_code import (
    TeaCodeType,
    StuCodeType,
    UserType,
)

from apps.utils.boss_utils import (
    Constructor,
)

TEA_LOWER_CODE = [c.lower() for c in TeaCodeType.All.value]
STU_LOWER_CODE = [c.lower() for c in StuCodeType.All.value]
DATE_TYPES = ['add', 'open', 'cancel', 'fee']


class MobileBossAPI(Resource):

    @staticmethod
    def get():
        """
        说明：用户登录
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        Zuyong Du         2018-10-22
        ----------------------------------------
        """
        return json_response()

    @staticmethod
    def post():
        """
        说明：boss 统计分析查询
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        王建彬         2018-10-22
        ----------------------------------------
        """
        # 参数获取
        parser = reqparse.RequestParser()
        parser.add_argument(
            "begin_ts",
            type=int,
            required=True,
            location=['form', 'json'],
            help="参数错误: begin_ts",
        )
        parser.add_argument(
            "end_ts",
            type=int,
            required=True,
            location=['form', 'json'],
            help="参数错误: end_ts",
        )
        parser.add_argument(
            "user_type",
            type=int,
            required=True,
            location=['form', 'json'],
            choices=UserType.All.value,
            help="参数错误: user_type",
        )

        params = parser.parse_args()
        q = Query(params=params, table='statist_mobile_boss')
        data = q.data

        return json_response(data=data, msg='ok')


class Query(object):
    """
    说明：查询封装
    --------------------------------
    修改人    修改日期         修改原因
    --------------------------------
    王建彬    2018-10-17
    --------------------------------
    """

    def __init__(
            self,
            params: Dict,
            table: str,
    ) -> None:
        # 添加日期类型列表
        self.date_types = DATE_TYPES

        # 添加用户类型列表
        self.code_types = {
            UserType.Stu.value: STU_LOWER_CODE,
            UserType.Tea.value: TEA_LOWER_CODE,
        }.get(params.get('user_type'))

        # 设置sql查询条件
        self._cond = Constructor()
        self.__set_cond(params, table)
        # 设置日期轴
        self.__set_date_axis(params)

    # 设置sql查询条件
    def __set_cond(
            self,
            params: Any,
            table: str,
    ) -> None:
        # 添加sql查询表名
        self._cond.update(table=table)

        # 获取起止时间戳
        begin_ts = params.get('begin_ts')
        end_ts = params.get('end_ts')

        # 日期转换并添加
        begin_day = datetime.datetime.fromtimestamp(begin_ts).strftime('%Y%m%d')
        end_day = datetime.datetime.fromtimestamp(end_ts).strftime('%Y%m%d')
        self._cond.update(
            begin_day=begin_day,
            end_day=end_day,
        )

        # 设置科目字段类型
        field_types = []
        for date in self.date_types:
            for code in self.code_types:
                field = f'{date}_{code}'
                sum_field = f'SUM({field}) AS {field}'
                field_types.append(sum_field)

        self._cond.update(code_field=',\n'.join(field_types))

    # 设置日期轴
    def __set_date_axis(
            self,
            params: Any,
    ) -> None:
        # 获取起止时间戳
        begin_ts = params.get('begin_ts')
        end_ts = params.get('end_ts')

        # 获取日期差
        begin = datetime.datetime.fromtimestamp(begin_ts)
        end = datetime.datetime.fromtimestamp(end_ts)
        day_count = (end - begin).days

        # 设置时间轴列表
        date_axis = []
        for n in range(day_count + 1):
            date = begin + datetime.timedelta(n)
            axis = date.strftime('%m-%d')

            date_axis.append(axis)

        self.date_axis = date_axis

    # 数据查询和拼接
    @property
    def data(self) -> Dict:
        query = self._query_fetch()
        legend = self._legend_with_sort()

        show = self._positive_for_query(query)
        if show:
            series = self._series_with_sort(query, legend)
            conf = dict(
                legend=legend,
                series=series,
                xAxis=self.date_axis,
            )
        else:
            conf = {}

        data = dict(conf=conf, show=show)

        return data

    def _query_fetch(self) -> List:
        c = self._cond
        data_day = 'data_day'
        sql = f"""
            SELECT 
                {data_day},
                {c.code_field}
            FROM 
                tbkt_statistics.{c.table} 
            WHERE 
                {data_day} BETWEEN {c.begin_day} AND {c.end_day}
            GROUP BY 
                {data_day}
        """
        query = list(db.get_engine(bind="statist").execute(sql))
        return query

    # 类别名称获取
    @staticmethod
    def _legend_with_sort() -> List[str]:
        # 获取科目名称
        code_name = (
            '数学',
            '物理',
            '化学',
            '英语',
            '语文',
        )

        # 获取日期类型名称
        date_name = (
            '录入',
            '开通',
            '退订',
            '计费',
        )

        # 添加类型名称
        legend = []
        for d in date_name:
            for c in code_name:
                name = d + c
                legend.append(name)

        return legend

    # 获取类别详细数据配置
    def _series_with_sort(
            self,
            query: List,
            legend: List,
    ) -> Dict[str, Dict]:
        # 数据翻转90度
        r_table = list(zip(*query))[1:]

        series = {}
        for d, date in enumerate(self.date_types):
            stack = date
            for c, code in enumerate(self.code_types):
                # 获取索引位置
                idx = d * 5 + c

                # 根据索引获取名称和数据
                name = legend[idx]
                data = r_table[idx]

                # 把数据中的decimal转化为str
                fmt_data = [str(i) for i in data]

                # 设置每个柱条配置
                conf = dict(
                    name=name,
                    type='bar',
                    stack=stack,
                    data=fmt_data,
                )

                series[name] = conf

        return series

    # 获取数据是否全部为0
    @staticmethod
    def _positive_for_query(query: List) -> bool:
        r_table = list(zip(*query))[1:]

        for row in r_table:
            for num in row:
                if num > 0:
                    return True

        return False
