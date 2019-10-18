# coding=utf-8
from flask_restful import Resource, reqparse
from apps.utils.pool_db import db
from apps.utils.db import  neo
# from utils.json_resp import json_response

class UserLogin(Resource):

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
        data = db.default.demo.select("name").get(id=1)
        print(data)
        return "dddddddddddddddddddd"


class Test_Data(Resource):

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
        sql = """select * from L_AcDbLayerTable limit 10"""
        data = db.lifan.fetchall_dict(sql)

        print(data)
        # data = neo.fetchall()
        # # nodes = neo.nodes
        # # n = nodes.match("Home_Test", name="men")
        # # print(n)
        # a = neo.run("create (n:people{name:'小明孙',age:'18',sex:'女'}) return n;")
        # # data = db.default.demo.select("name").get(id=1)
        # print(a['id'])
        return data


from apps.utils.page import Pagination
from flask import render_template


class Data_Page(Resource):

    @staticmethod
    def get():
        li = []
        for i in range(1,100):
            li.append(i)
        # print(li)
        pager_obj = Pagination(request.args.get("page",1),len(li),request.path,request.args,per_page_count=10)
        # print(request.args)
        index_list = li[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template("pager.html",index_list=index_list, html = html,condition=path)