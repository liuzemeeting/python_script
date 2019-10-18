import os
import pymysql
import json
from .db import Hub
db = Hub(pymysql)
# 当前文件路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 当前文件上级路径
ENV_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

DB_WAIT_TIMEOUT = 29  # 单个连接最长维持时间
DB_POOL_SIZE = 8  # 连接池最大连接数
# 数据库字典集合
DATABASES = {
    "default": {
        "DB_NAME": "test",
        "DB_HOST": "192.168.99.100",
        "DB_USER": "root",
        "DB_PASS": "123456",
        "DB_PORT": "3306",
    },
    "lifan": {
        "DB_NAME": "dwg",
        "DB_HOST": "192.168.99.96",
        "DB_USER": "root",
        "DB_PASS": "123456",
        "DB_PORT": "3306",
    }
}

# 初始化db数库链接方式
for table, db_param in DATABASES.items():
    db.add_pool(
        table,
        db=db_param["DB_NAME"],
        host=db_param["DB_HOST"],
        user=db_param["DB_USER"],
        passwd=db_param["DB_PASS"],
        port=int(db_param["DB_PORT"]),
        charset='utf8mb4',
        autocommit=True,
        pool_size=DB_POOL_SIZE,
        wait_timeout=DB_WAIT_TIMEOUT
    )