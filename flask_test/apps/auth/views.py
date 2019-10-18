# coding=utf-8
import uuid
import time
from collections import defaultdict
from flask_restful import Resource, reqparse
from flask import current_app
from apps.statist.common.task_common import Struct
from apps.utils.res import json_response
from werkzeug.security import check_password_hash

from application import db

# 登录失败次数限制
login_limit = defaultdict(int)


def fetchall(engine, sql):
    return [Struct(dict(zip(i.keys(), i))) for i in engine.execute(sql).fetchall()]


class UserLogin(Resource):

    @staticmethod
    def get():
        """
        说明：用户登录
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        Zuyong Du         2018-10-22
        ----------------------------------------
        """
        res = db.get_engine(bind="statist").execute("select * from login_city")
        # res = db.engine.execute("select * from login_city")
        print(res)
        for row in res:
            data = {k: v for k, v in row.items()}
            print(data)
        return json_response()

    @staticmethod
    def post():
        """
        说明：用户登录
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        Zuyong Du         2018-10-22
        ----------------------------------------
        """
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, help="请输入账号")
        parser.add_argument("password", required=True, help="请输入密码")
        args = parser.parse_args()
        # 获取参数值
        username = args.username
        password = args.password
        user = User.query.filter_by(username=username).first()
        if user:
            if user.is_active:
                if user.check_password(password):
                    token = uuid.uuid4().hex
                    user.access_token = token
                    user.token_expired = time.time() + 8 * 60 * 60  # 过期时间
                    user.save(commit=True)
                    data = {'nickname': user.nickname, 'token': token, 'is_supper': user.is_supper,
                            'permissions': list(user.permissions)}
                    return json_response(data={'nickname': user.username, 'token': token, 'is_supper': user.is_supper,
                                               'permissions': list(user.permissions)})
                else:
                    login_limit[username] += 1
                    if login_limit[username] >= 3:
                        user.update(is_active=False, commit=True)
                    return json_response(msg='用户名或密码错误，连续3次错误将会被禁用')
            else:
                return json_response(msg='用户已被禁用，请联系管理员')
        elif login_limit[username] >= 3:
            return json_response(msg='用户已被禁用，请联系管理员')
        else:
            login_limit[username] += 1
            return json_response(msg='用户名或密码错误，连续3次错误将会被禁用')


class NewUserLogin(Resource):

    @staticmethod
    def post():
        """
        说明：用户登录
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        liushiqi         2018-10-22
        ----------------------------------------
        """
        context = {}
        parser = reqparse.RequestParser()
        parser.add_argument("username", required=True, help="请输入账号")
        parser.add_argument("password", required=True, help="请输入密码")
        args = parser.parse_args()
        # 获取参数值
        username = args.username
        password = args.password
        sql = """
            select * from account_users where username = '%s'            
        """ % username
        user = fetchall(db.get_engine(bind="statist"), sql)
        if user:
            context['user_id'] = user[0].id
            context['user_name'] = user[0].nickname
            if check_password_hash(user[0].password_hash, password):
                return json_response(msg='登录成功！', data=context)
            else:
                return json_response(code='500', msg='账号或密码错误！')

        else:
            return json_response(code='500', msg='用户不存在！')
