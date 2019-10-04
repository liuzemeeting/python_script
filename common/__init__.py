# coding: utf-8
from .db import Hub
import pymysql

db = Hub(pymysql)


db_config = {
    "home": dict(
                host="116.255.220.101",
                port=3369,
                user="wangzehua",
                passwd="zEHaU@v381!w",
                db="tbkt_home",
    ),
    "tournament": dict(
                host="116.255.220.101",
                port=3369,
                user="wangzehua",
                passwd="zEHaU@v381!w",
                db="tbkt_tournament",
    ),
    "task": dict(
                host="59.110.54.105",
                port=3307,
                user="wangzehua",
                passwd="zehua2018@tbkt!",
                db="tbkt_task",
    ),
    "activity": dict(
                host="59.110.54.105",
                port=3307,
                user="wangzehua",
                passwd="zehua2018@tbkt!",
                db="tbkt_activity",
    )
}

for alias, config in db_config.items():
    db.add_pool(
        alias,
        host=config['host'],
        port=config['port'],
        user=config['user'],
        passwd=config['passwd'],
        db=config['db'],
        charset='utf8',
        autocommit=True,
        pool_size=16,
        wait_timeout=29
    )
