# coding=utf-8
# @Time    : 2018/10/22 下午3:24
# @Author  : Zuyong Du
import time
# from flask_socketio import SocketIO, emit

from flask import Flask, Blueprint, make_response, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask import request, g

from config import DefaultConfig
# 数据库连接
db = SQLAlchemy()
# Migrations
# CSRF
csrf = CSRFProtect()

# Flask实例
app = None


def create_app(config=None):
    """
    说明：创建flask应用
    :param config: 配置文件
    """
    global app
    global socketio
    app = Flask(__name__)

    # 使用默认配置
    app.config.from_object(DefaultConfig)
    # 更新配置
    app.config.from_object(config)
    # 蓝图注册
    configure_blueprints(app)
    db.init_app(app)

    app.before_request(cross_domain_access_before)
    # app.before_request(config_before_request)
    app.after_request(cross_domain_access_after)
    app.register_error_handler(Exception, exception_handler)
    app.register_error_handler(404, page_not_found)

    return app


def configure_blueprints(app):
    """
    说明：上下文注册蓝图
    :param app: app
    """
    api_url_prefix = app.config['API_URL_PREFIX']

    def register_module_bp(model_obj, model_name, suffix_='api', url_prefix_=api_url_prefix):
        """
        注册蓝图
        """
        # 若包模块有标识符__load_app或_load_api且为True，则此模块注册，否则忽略
        load_flag_name = "_load_{}".format(suffix_)
        # print(1,model_obj, model_name, load_flag_name,getattr(model_obj, load_flag_name))
        if not (hasattr(model_obj, load_flag_name) and getattr(model_obj, load_flag_name) is False):
            model_bp_name = "{}_{}_bp".format(model_name, suffix_)
            # print(model_obj, model_bp_name)
            if hasattr(model_obj, model_bp_name):
                model_bp = getattr(model_obj, model_bp_name)
                # print('model_bp', model_bp)
                if isinstance(model_bp, Blueprint) and model_bp not in app.blueprints:
                    # print(2, 'model_bp', model_bp_name, model_bp, url_prefix_)
                    app.register_blueprint(model_bp, url_prefix=url_prefix_)
    # 蓝图注册方式一，自动注册
    import pkgutil
    import importlib
    import apps
    package_path = apps.__path__
    package_name = apps.__name__
    import_error_bps = []
    for _, name, status in pkgutil.iter_modules(package_path):
        try:
            m = importlib.import_module('{0}.{1}'.format(package_name, name))
        except ImportError as e:
            import_error_bps.append((package_name, name))
            app.logger.error(
                "package_path:{}, package_name:{}, model_name:{}, except:{}\n{}, {}".format(package_path, package_name,
                                                                                            name,
                                                                                            e, _, status))
            continue
        else:
            register_module_bp(m, name, suffix_='api', url_prefix_=api_url_prefix)
    for v in import_error_bps:
        package_name, name = v
        m = importlib.import_module('{0}.{1}'.format(package_name, name))
        register_module_bp(m, name,  suffix_='api', url_prefix_=api_url_prefix)


def app_white_list():
    """
    说明：白名单地址，匿名用户可以访问
    """
    url_tuple = ('/api/login/')
    return url_tuple


def cross_domain_access_before():
    """
    说明：跨域请求对OPTIONS请求处理
    """
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'X-TOKEN'
        response.headers['Access-Control-Allow-Headers'] = 'X-PROJID'
        response.headers['Access-Control-Allow-Headers'] = 'X-CLUSTERID'
        response.headers['Access-Control-Max-Age'] = 24 * 60 * 60
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
        return response


def cross_domain_access_after(response):
    """
    说明：跨域请求 之后  增加header相关信息
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-TOKEN, X-PROJID, X-CLUSTERID'
    return response


def page_not_found(_):
    """
    说明：404页面
    """
    from apps.utils.res import json_response

    return json_response(msg='Page not found'), 404


def exception_handler(ex):
    """全局异常处理"""
    import traceback
    from apps.utils.res import json_response
    ex_message = traceback.print_exc()
    app.logger.error(ex_message)
    message = '%s' % ex
    if len(message) > 60:
        message = message[:60] + '...'
    return json_response(code=500, msg=message)


def config_before_request():
    """
    说明：请求拦截
    """
    from apps.utils.res import json_response, ResCode
    print('config_before_requestdddd')
    if current_app.config["TOKEN_AUTH"]:
        white_flag = False   # 白名单标识
        for url in app_white_list():
            if request.path.startswith(url):
                white_flag = True
                break
        if not white_flag:
            # print(request.headers)
            token = request.headers.get("X-TOKEN", '')
            if request.method in ['PUT', 'POST', 'DELETE']:
                # 保存操作历史
                pass
            return json_response(code=ResCode.RES_FALSE), 401

