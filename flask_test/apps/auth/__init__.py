# coding=utf-8
# @Time    : 2018/10/22 下午3:24
# @Author  : Zuyong Du

from flask import Blueprint
from flask_restful import Api, reqparse

from .views import UserLogin,NewUserLogin


auth_api_bp = Blueprint('auth', __name__)
auth = Api(auth_api_bp)

auth.add_resource(UserLogin, '/login/')
auth.add_resource(NewUserLogin, '/new_login/')
_load_api = True
