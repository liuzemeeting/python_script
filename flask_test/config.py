# coding=utf-8
# @Time    : 2018/10/22 下午3:24
# @Author  : Zuyong Du
import os
import json


class DefaultConfig(object):
    # 启动端口
    PORT = 5001
    # 主机
    HOST = "0.0.0.0"
    # 是否启用接口
    API_ENABLE = True
    # 接口前缀
    API_URL_PREFIX = "/api"
    # 是否启用token验证
    TOKEN_AUTH = False
    # TOKEN 过期时间默认2天
    APP_TOKEN_EXPIRE = 7 * 24 * 60 * 60

    SECRET_KEY = 'secret!'


class DevelopmentConfig(DefaultConfig):
    # 调试模式开关
    DEBUG = True
    TESTING = False
    # Mysql数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/dwg' % (
        "root",
        "123456",
        "192.168.0.125",
        3306)
    # SQLALCHEMY_BINDS = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 50
    # 指定数据库连接池的超时时间。默认是 10s
    SQLALCHEMY_POOL_TIMEOUT = 10
    # 配置连接池的连接recyle时间设的小一点。默认7200s
    SQLALCHEMY_POOL_RECYCLE = 10
    # 设置数据库中字符串编码格式（针对mysql数据库）
    # SQLALCHEMY_DATABASE_CHAR_CODE = u"utf8_general_ci"

    SQLALCHEMY_BINDS = {
        'default': 'mysql+pymysql://%s:%s@%s:%s/dwg' % (
            "root",
            "123456",
            "192.168.0.125",
            3306
        )
    }
