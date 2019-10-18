# coding=utf-8
# @Time    : 2018/10/22 下午3:24
# @Author  : Zuyong Du

from flask import Blueprint
from flask_restful import Api, reqparse

from apps.statist import city_school, open_data
from apps.statist.money_data import MoneyDataAPI
# from apps.statist.tbkt_task import TbktTaskAPI
from .boss import BossAPI
from .mobile_boss import MobileBossAPI
from .sms import SmsAPI
from .sms import SmsDetailAPI
from .sms import SmsFailAPI
from .task_stu import TaskStuAPI
from .task_tea import TaskTeaAPI
from .login import LoginAPI
from .expand import ExpandApi
from .simplify_boss import SimplifyBossAPI

# from .redmine import RedmineAPI


statist_api_bp = Blueprint('statist', __name__)
auth = Api(statist_api_bp)

# Boss统计
auth.add_resource(BossAPI, '/statist/boss/')
# 移动Boss统计
auth.add_resource(MobileBossAPI, '/statist/mobileboss/')
# 短信统计
auth.add_resource(SmsAPI, '/statist/sms/')
# 短信统计查看详情
auth.add_resource(SmsDetailAPI, '/statist/sms/detail/')
# 短信统计查看失败详情
auth.add_resource(SmsFailAPI, '/statist/sms/fail/')
# 学生做作业统计
auth.add_resource(TaskStuAPI, '/statist/task/stu/')
# 教师发作业统计
auth.add_resource(TaskTeaAPI, '/statist/task/tea/')
# 登录业统计
auth.add_resource(LoginAPI, '/statist/login/')
# 课外拓展业统计
auth.add_resource(ExpandApi, '/statist/expand/')

# 同步课堂任务统计
# auth.add_resource(TbktTaskAPI, '/statist/tbkt/task')

# simplify_Boss统计
auth.add_resource(SimplifyBossAPI, '/statist/simplify_boss/')

auth.add_resource(city_school.City, '/statist/city/')
auth.add_resource(city_school.School, '/statist/school/')
auth.add_resource(open_data.OpenDays, '/statist/open/days/')
auth.add_resource(open_data.OpenCitySchool, '/statist/open/city/')
# 计费金额统计
auth.add_resource(MoneyDataAPI, '/statist/money/')

_load_api = True


