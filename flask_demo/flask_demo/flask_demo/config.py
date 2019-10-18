# coding=utf-8
# @Time    : 2019/10/14 下午3:24
# @Author  : wangzehua
import os
import json


class DefaultConfig(object):
    # 启动端口
    PORT = 5002
    # 主机
    HOST = "0.0.0.0"
    # 是否启用接口
    API_ENABLE = True
    # 接口前缀
    # API_URL_PREFIX = "api"
    # 是否启用token验证
    TOKEN_AUTH = False
    # TOKEN 过期时间默认2天
    APP_TOKEN_EXPIRE = 7 * 24 * 60 * 60

    SECRET_KEY = 'secret!'


class DevelopmentConfig(DefaultConfig):
    # 调试模式开关
    DEBUG = True
    TESTING = True
    # 项目目录路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
