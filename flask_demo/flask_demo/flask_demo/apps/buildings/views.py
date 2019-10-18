# coding=utf-8
from flask_restful import Resource, reqparse
from apps.utils.pool_db import db
from apps.utils.db import  neo
# from utils.json_resp import json_response


class Create_Realation(Resource):

    @staticmethod
    def get():
        """
        说明：用户登录
        """
        return "dddddddddddddddddddd"

    @staticmethod
    def post():
        """
        说明：用户登录
        """
        sql = """select * from demo"""
        data = db.default.fetchall_dict(sql)

        print(data)
        # data = db.default.demo.select("name").get(id=1)
        # print(data)
        # a = neo.run("create (n:people{name:'小明孙',age:'18',sex:'女'}) return n;")
        # # data = db.default.demo.select("name").get(id=1)
        # print(a['id'])
        return "dddddddddddddddddddd"
