# coding=utf-8
# @Time    : 2018/10/22 下午3:24
# @Author  : Zuyong Du

from flask_script import Manager, Server

from config import DevelopmentConfig as Config
from application import create_app


app = create_app(Config)
manager = Manager(app)


# 运行本地服务
manager.add_command("runserver", Server(app.config["HOST"], port=app.config["PORT"], passthrough_errors=True))


if __name__ == "__main__":
   
    manager.run()