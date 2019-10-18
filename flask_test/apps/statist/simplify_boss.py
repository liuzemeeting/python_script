import datetime
import logging

from flask_restful import Resource, reqparse

from application import db
from apps.utils.res import json_response

log = logging.getLogger(__name__)


class SimplifyBossAPI(Resource):

    @staticmethod
    def get():
        """
        说明：boss 统计分析
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        刘士奇         2019-2-22
        ----------------------------------------
        """
        return json_response()

    @staticmethod
    def post():
        """
        说明：boss 统计分析
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        刘士奇         2019-2-22
        ----------------------------------------
        """
        # 获取参数值
        parser = reqparse.RequestParser()
        parser.add_argument("user_type")
        parser.add_argument("begin_time")
        parser.add_argument("end_time")
        args = parser.parse_args()
        begin_time_str = args.begin_time
        end_time_str = args.end_time
        user_type = args.user_type
        begin_time_sql = begin_time_str.replace('-', '')
        end_time_sql = end_time_str.replace('-', '')
        month_list = get_month_range(begin_time_str, end_time_str)
        if user_type == '1':  # 学生
            sim_sql = f"""
                SELECT
                    CONCAT(
                        YEAR (data_day),
                        '-',
                        MONTH (data_day)
                    ) AS date_str,
                    SUM(add_a) AS add_a,
                    SUM(add_b) AS add_b,
                    SUM(add_c) AS add_c,
                    SUM(add_d) AS add_d,
                    SUM(add_e) AS add_e,
                    SUM(open_a) AS open_a,
                    SUM(open_b) AS open_b,
                    SUM(open_c) AS open_c,
                    SUM(open_d) AS open_d,
                    SUM(open_e) AS open_e,
                    SUM(cancel_a) AS cancel_a,
                    SUM(cancel_b) AS cancel_b,
                    SUM(cancel_c) AS cancel_c,
                    SUM(cancel_d) AS cancel_d,
                    SUM(cancel_e) AS cancel_e
                FROM
                    tbkt_statistics.statist_boss
                WHERE
                    data_day BETWEEN {begin_time_sql} AND {end_time_sql}
                GROUP BY
                    YEAR (data_day),MONTH (data_day);
                """
        else:  # 教师
            sim_sql = f"""
                SELECT
                    CONCAT(
                        YEAR (data_day),
                        '-',
                        MONTH (data_day)
                    ) AS date_str,
                    SUM(add_j) AS add_j,
                    SUM(add_k) AS add_k,
                    SUM(add_l) AS add_l,
                    SUM(add_m) AS add_m,
                    SUM(add_n) AS add_n,
                    SUM(open_j) AS open_j,
                    SUM(open_k) AS open_k,
                    SUM(open_l) AS open_l,
                    SUM(open_m) AS open_m,
                    SUM(open_n) AS open_n,
                    SUM(cancel_j) AS cancel_j,
                    SUM(cancel_k) AS cancel_k,
                    SUM(cancel_l) AS cancel_l,
                    SUM(cancel_m) AS cancel_m,
                    SUM(cancel_n) AS cancel_n
                FROM
                    tbkt_statistics.statist_boss
                WHERE
                    data_day BETWEEN {begin_time_sql} AND {end_time_sql}
                GROUP BY
                    YEAR (data_day),MONTH (data_day);
                """
        sim_boss_query = list(db.get_engine(bind="statist").execute(sim_sql))
        boss_map = {str(row[0]): row[1:] for row in sim_boss_query}
        # 数据整理
        query = []
        for month in month_list:
            # 根据时间获取boss数据
            boss_row = boss_map.get(month, [0] * 15)
            # 添加数据
            row = [month] + list(boss_row)
            query.append(row)
        legend = get_legend()
        show = positive_for_query(query)
        if show:
            series = series_with_sort(query, legend)
            conf = dict(
                legend=legend,
                series=series,
                xAxis=month_list,
            )
        else:
            conf = {}
        data = dict(conf=conf, show=show)
        return json_response(data=data, msg='ok')


def get_month_range(start_day, end_day):
    """
    获取两个日期之间的月份数组
    :param start_day: 开始日期 (2000-01-01)
    :param end_day: 截止提起 (2000-01-01)
    :return: 月份数组
    """
    start_day = datetime.date(*map(int, start_day.split('-')))
    end_day = datetime.date(*map(int, end_day.split('-')))
    months = (end_day.year - start_day.year) * 12 + end_day.month - start_day.month
    month_range = ['%s-%s' % (start_day.year + mon // 12, mon % 12 + 1)
                   for mon in range(start_day.month - 1, start_day.month + months)]
    return month_range


def get_legend():
    # 获取科目名称
    code_name = ('数学', '物理', '化学', '英语', '语文')
    # 获取boss名称
    boss_name = ('录入', '开通', '退订')
    # 添加类型名称
    legend = []
    for b in boss_name:
        for c in code_name:
            name = b + c
            legend.append(name)
    return legend


def positive_for_query(query):
    """
    获取数据是否全部为0
    :param query: 数据源
    :return:
    """
    r_table = list(zip(*query))[1:]
    for row in r_table:
        for num in row:
            if num > 0:
                return True

    return False


def series_with_sort(query, legend):
    """
    获取类别详细数据配置
    :param query:
    :param legend:
    :return:
    """
    # 数据翻转90度
    r_table = list(zip(*query))[1:]
    series = {}
    # 添加科目数据
    types = ['add', 'open', 'cancel']
    code_type = ['a', 'b', 'c', 'd', 'e']
    for t in range(len(types)):
        for c in range(len(code_type)):
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
                stack=types[t] + code_type[c],
                data=fmt_data,
            )
            series[name] = conf
    return series
