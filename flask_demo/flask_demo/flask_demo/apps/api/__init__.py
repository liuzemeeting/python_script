
from flask import Blueprint
from flask_restful import Api, reqparse

from apps.api.views import UserLogin, Test_Data
_load_api = True

api_api_bp = Blueprint('auth', __name__)
auth = Api(api_api_bp)
auth.add_resource(UserLogin, '/login/')
auth.add_resource(Test_Data, '/test/')