# @File  : open_data.py
# @Author: 王世成
# @Date  : 2019/3/14
# @Desc  : 开通数据统计
import calendar
import datetime
from collections import defaultdict

from flask_restful import Resource, reqparse

from application import db
from apps.statist.common.task_common import Struct
from apps.utils.res import json_response


class OpenCommon(Resource):
    def series_format(self, data):
        series = defaultdict(list)
        for i in data:
            for k, v in i.items():
                name = self.get_name(k)
                if not name:
                    continue
                series[(name, k, 'bar')].append(v)
        series_data = {}
        for (name, key, typ), lst in series.items():
            series_data[name] = dict(
                name=name,
                type=typ,
                stack=key,
                data=[i or 0 for i in lst],
                markPoint={
                    "data": [
                        {"type": 'max', "name": '最大值'},
                        {"type": 'min', "name": '最小值'}
                    ]
                }
            )
        return series_data

    @staticmethod
    def get_name(k):
        prefix_dict = {"total": "开通", "incr": "净增", "cancel": "退订"}
        code_dict = {"a": "数学", "b": "物理", "c": "化学", "d": "英语", "e": "语文"}
        temp = k.split("_")
        if len(temp) <= 1 or temp[0] not in prefix_dict:
            return
        return code_dict[temp[1]]+prefix_dict[temp[0]]

    @staticmethod
    def fetchall(engine, sql):
        return [Struct(dict(zip(i.keys(), i))) for i in engine.execute(sql).fetchall()]

    @staticmethod
    def make_cond(*args):
        return " and ".join([i for i in args if i])

    @staticmethod
    def make_date_sql(select_type, begin_date, end_date):
        days = [begin_date]
        month = []
        dt = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        date = begin_date[:]
        while date <= end_date:
            dt += datetime.timedelta(days=1)
            date = dt.strftime("%Y-%m-%d")
            if select_type == 1:
                days.append(date)
            else:
                _, days = calendar.monthrange(dt.year, dt.month)
                end_month = dt.strftime(f"%Y-%m-{days}")
                if end_month not in month:
                    month.append(end_month)
        sql = []
        for i in days if select_type == 1 else month:
            sql.append(f" select '{i}' date1 \n")
        return "union".join(sql)


class OpenDays(OpenCommon):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("select_type", type=int, required=True, help="请选择查询类型", location=['form', 'json'])
        parser.add_argument("start_date", required=False, location=['form', 'json'])
        parser.add_argument("end_date", required=False, location=['form', 'json'])
        args = parser.parse_args()

        start_date = args.start_date
        end_date = args.end_date

        if start_date and end_date:
            sql = f"""
            select * from statist_open_day d right join 
            ({self.make_date_sql(args.select_type, start_date, end_date)}) t
            on d.date = t.date1 and type = {args.select_type} order by t.date1
            """
        else:
            sql = f"select * from statist_open_day d where d.type = {args.select_type} order by d.date limit 7"
        print(sql)
        data = self.fetchall(db.get_engine(bind="statist"), sql)
        out = Struct()
        out.xAxis = [i.date1 for i in data] if start_date and end_date else [i.date.strftime("%Y-%m-%d") for i in data]
        out.series = self.series_format(data)
        return json_response(data=out, msg='ok')


class OpenCitySchool(OpenCommon):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("city_id", type=str, location=['form', 'json'])
        parser.add_argument("county_id", type=str, location=['form', 'json'])
        parser.add_argument("school_id", type=str, location=['form', 'json'])
        parser.add_argument("select_type", type=int, required=True, choices=[1, 2], location=['form', 'json'])
        parser.add_argument("start_date", location=['form', 'json'])
        parser.add_argument("end_date", location=['form', 'json'])
        args = parser.parse_args()

        start_date = args.start_date
        end_date = args.end_date
        city_cond = f" city_id = {args.city_id} " if args.city_id else ""
        county_cond = f" county_id = {args.county_id} " if args.county_id else ""
        school_cond = f" school_id = {args.school_id} " if args.school_id else ""

        cond = ""
        if start_date and end_date:
            cond = " date between '%s' and '%s' " % (start_date, end_date)
            date_sql = self.make_date_sql(args.select_type, start_date, end_date)

        if school_cond:
            table_name = {
                1: "statist_open_school_day",
                2: "statist_open_school_month"
            }.get(args.select_type)
            if not cond:
                sql = f"""
                select * from {table_name} d where {school_cond} order by date limit 7
                """
            else:
                sql = f"""
                select * from {table_name} d right join 
                ({date_sql}) t on d.date = t.date1 
                and {self.make_cond(school_cond, cond)} order by date1
                """

        elif county_cond:
            if not cond:
                sql = f"""
                select * from statist_open_county d where d.type = {args.select_type} 
                and {county_cond} order by date limit 7
                """
            else:
                sql = f"""
                select * from statist_open_county d right join 
                ({date_sql}) t
                on d.date = t.date1 and type = {args.select_type} and
                {county_cond} order by date1
                """

        elif city_cond:
            if not cond:
                sql = f"""
                select * from statist_open_city d where d.type = {args.select_type} 
                and {city_cond} order by date limit 7
                """
            else:
                sql = f"""
                select * from statist_open_city d right join 
                ({date_sql}) t
                on d.date = t.date1 and type = {args.select_type} and
                {city_cond} order by date1
                """
        data = self.fetchall(db.get_engine(bind="statist"), sql)
        out = Struct()
        out.xAxis = [i.date1 for i in data] if cond else [i.date.strftime("%Y-%m-%d") for i in data]
        out.series = self.series_format(data)
        return json_response(data=out, msg='ok')
