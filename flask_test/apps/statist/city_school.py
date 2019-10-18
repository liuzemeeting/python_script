# @File  : city_school.py
# @Author: 王世成
# @Date  : 2019/3/11
# @Desc  :
from flask_restful import Resource, reqparse

from application import db
from apps.statist.common.task_common import Struct
from apps.utils.res import json_response

city = []


def fetchall(engine, sql):
    return [Struct(dict(zip(i.keys(), i))) for i in engine.execute(sql).fetchall()]


class City(Resource):
    def get(self):
        global city
        engine = db.get_engine(bind="base")
        if not city:
            sql = """
            SELECT
                cityId,
                name,
                fatherId 
            FROM
                common_provincecity 
            WHERE
                path LIKE '410000%%' 
                AND fatherId != 0
            """
            city = self.data_format(fetchall(engine, sql))
        return json_response(data=city, msg='ok')

    def data_format(self, data, father_id='410000'):
        children = [c for c in data if c.fatherId == father_id]
        result = []
        for c in children:
            c.children = self.data_format(data, father_id=c.cityId)
            result.append(c)
        return result


class School(Resource):

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument("county_id", required=True, help="请选择区县")
        args = parser.parse_args()
        # 获取参数值
        county_id = args.county_id
        sql = """
        select id school_id, name school_name from school where county = %s and type <= 2 and status = 1
        """ % county_id
        data = fetchall(db.get_engine(bind="base"), sql)
        return json_response(data=data, msg='ok')
