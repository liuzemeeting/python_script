# coding=utf-8
# @Time    : 2018/10/22 下午3:24
# @Author  : Zuyong Du

from config import DevelopmentConfig as Config
from application import create_app

app = create_app(Config)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=False, threaded=True)