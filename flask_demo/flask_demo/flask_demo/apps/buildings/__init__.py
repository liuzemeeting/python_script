
from flask import Blueprint
from flask_restful import Api, reqparse

from apps.buildings.views import Create_Realation
print("ddddddddddd")
_load_api = True

buildings_api_bp = Blueprint('build', __name__)
auth = Api(buildings_api_bp)
print("auth", auth)
auth.add_resource(Create_Realation, '/create/')

