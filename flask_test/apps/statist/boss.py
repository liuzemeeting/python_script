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
    array_day_from_range,
)

TEA_LOWER_CODE = [c.lower() for c in TeaCodeType.All.value]
STU_LOWER_CODE = [c.lower() for c in StuCodeType.All.value]
BOSS_TYPES = ['add', 'open', 'cancel', 'fee']
FTP_TYPES = ['open', 'cancel', 'code']
FTP_SUM_FIELDS = [
    'resp_total',
    'resp_open_num',
    'resp_cancel_num',
    'resp_code_open_num',
]


class BossAPI(Resource):

    @staticmethod
    def get():
        """
        说明：boss 统计分析
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
        q = Query(params=params)
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
    ) -> None:
        # 添加boss类型列表
        self.boss_types = BOSS_TYPES

        # 添加移动报文类型列表
        self.ftp_types = FTP_TYPES

        # 添加用户类型列表
        self.code_types = {
            UserType.Stu.value: STU_LOWER_CODE,
            UserType.Tea.value: TEA_LOWER_CODE,
        }.get(params.get('user_type'))

        self.stu_types = STU_LOWER_CODE

        # 设置sql查询条件
        self._cond = Constructor()
        self.__set_cond(params)
        # 设置日期轴
        self.__set_date_axis(params)

    # 设置sql查询条件
    def __set_cond(
            self,
            params: Any,
    ) -> None:
        # 添加sql查询表名
        self._cond.update(
            boss_table='statist_boss',
            ftp_table='statist_boss_ftpdata',
        )

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

        # 设置时间范围列表(存储每天格式化时间)
        self._day_range = array_day_from_range(
            int(begin_ts),
            int(end_ts),
        )

        # 设置boss科目字段类型
        boss_fields = []
        for boss in self.boss_types:
            for code in self.code_types:
                field = f'{boss}_{code}'
                sum_field = f'SUM({field}) AS {field}'
                boss_fields.append(sum_field)

        self._cond.update(boss_fields=',\n'.join(boss_fields))

        # 设置ftp科目字段类型
        ftp_fields = []
        for ftp in self.ftp_types:
            for code in self.stu_types:
                field = f'{ftp}_{code}'
                sum_field = f'SUM({field}) AS {field}'
                ftp_fields.append(sum_field)

        # 添加求和字段
        ftp_fields += FTP_SUM_FIELDS

        self._cond.update(ftp_fields=',\n'.join(ftp_fields))

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

        # 查询 boss 数据
        boss_sql = f"""
            SELECT 
                {data_day},
                {c.boss_fields}
            FROM 
                tbkt_statistics.{c.boss_table} 
            WHERE 
                {data_day} BETWEEN {c.begin_day} AND {c.end_day}
            GROUP BY 
                {data_day}
            order by 
                {data_day}
        """
        boss_query = list(db.get_engine(bind="statist").execute(boss_sql))
        boss_map = {str(row[0]): row[1:] for row in boss_query}

        # 查询 ftp 数据
        ftp_sql = f"""
            SELECT 
                {data_day},
                {c.ftp_fields}
            FROM 
                tbkt_statistics.{c.ftp_table} 
            WHERE 
                {data_day} BETWEEN '{c.begin_day}' AND '{c.end_day}'
            GROUP BY 
                {data_day}
            order by 
                {data_day}
        """
        ftp_query = list(db.get_engine(bind="statist").execute(ftp_sql))
        ftp_map = {str(row[0]): row[1:] for row in ftp_query}

        # 数据合并
        query = []
        boss_count = len(self.boss_types) * len(self.code_types)
        ftp_count = (len(self.ftp_types) * len(self.code_types)) + len(FTP_SUM_FIELDS)
        for day in self._day_range:
            # 根据day时间获取boss和ftp数据
            boss_row = boss_map.get(day, [0] * boss_count)
            ftp_row = ftp_map.get(day, [0] * ftp_count)

            # 添加记录
            row = [day] + list(boss_row) + list(ftp_row)
            query.append(row)

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

        # 获取boss和报文类型名称
        boss_name = (
            '录入',
            '开通',
            '退订',
            '计费',
            '移动开通请求',
            '移动退订请求',
            '移动验证码',
        )

        # 添加类型名称
        legend = []
        for b in boss_name:
            for c in code_name:
                name = b + c
                legend.append(name)

        legend += [
            '移动响应总数',
            '移动响应开通成功数',
            '移动响应退订成功数',
            '验证码移动响应成功数',
        ]

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

        # 添加科目数据
        types = self.boss_types + [f'ftp_{i}' for i in self.ftp_types]
        for t in range(len(types)):
            for c in range(len(self.code_types)):
                # 获取索引位置
                idx = t * 5 + c

                # 根据索引获取名称和数据
                name = legend[idx]
                data = r_table[idx]

                # 把数据中的decimal转化为str
                fmt_data = [str(i) for i in data]

                # 设置每个柱条配置
                conf = dict(
                    name=name,
                    type='bar',
                    stack=types[t],
                    data=fmt_data,
                )

                series[name] = conf

        # 添加求和数据
        sum_legend = legend[-4:]
        sum_row = r_table[-4:]
        for i in range(4):
            data = sum_row[i]
            name = sum_legend[i]
            fmt_data = [str(i) for i in data]

            conf = dict(
                name=name,
                type='bar',
                stack='ftp_sum',
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
