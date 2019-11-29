# coding: utf-8
import json
import os
import time
import datetime
import hashlib
from common import db
import requests


def get_upload_key():
    """
    功能:生成上传key
    """
    # 上传key
    now = datetime.datetime.now()
    m = hashlib.md5()
    key_var = '%s%s' % ('bannei_upload', now.strftime("%Y%m%d"))
    m.update(key_var.encode())
    return m.hexdigest()


def upload():
    icon_data = []
    attire_data = []
    url = "http://upload.m.xueceping.cn/swf_upload/?upcheck=" + get_upload_key() + "&upType=attire"
    for root, dirs, files in os.walk('sign_bg'):
        for i in files:
            files = {"field1": open(f"{root}/{i}", 'rb')}
            r = requests.post(url, files=files)
            response = json.loads(r.text.replace('\'', '"'))[0]
            file_name = response["file_name"]
            file_url = response["file_url"]
            name = file_name.split('.')[0]
            all_name = name.split('-')
            part_id = all_name[1]
            sex = all_name[2]
            d = {
                "attire_name": name,
                "part_id": part_id,
                "sex": sex,
                "icon_url": file_url
            }
            icon_data.append(d)
    for root, dirs, files in os.walk('sign_tc'):
        for i in files:
            files = {"field1": open(f"{root}/{i}", 'rb')}
            r = requests.post(url, files=files)
            response = json.loads(r.text.replace('\'', '"'))[0]
            file_name = response["file_name"]
            file_url = response["file_url"]
            name = file_name.split('.')[0]
            all_name = name.split('-')
            part_id = all_name[1]
            sex = all_name[2]
            d = {
                "part_id": part_id,
                "sex": sex,
                "file_url": file_url
            }
            attire_data.append(d)
    return icon_data, attire_data


if __name__ == '__main__':
    icon_data, attire_data = upload()
    print("icon_data", icon_data)
    print("attire_data", attire_data)
    reword_name = {1: "发饰", 2: "上衣", 3: "下衣", 4: "鞋子", 5: "场景"}
    reword_girl_name = {8: "发饰", 9: "上衣", 10: "下衣", 11: "鞋子", 12: "场景"}
    print("reword_name", reword_name)
    c_dict = {}
    for i in attire_data:
        key = str(i["part_id"]) + str(i["sex"])
        if key in c_dict:
            b = c_dict["%s"%key]
            attire_fair = i["file_url"]
            b += ",%s" % attire_fair
            c_dict["%s"%key] = b
        else:
            c_dict.update({key: i["file_url"]})
    print(c_dict)
    for item in icon_data:
        key = str(item["part_id"]) + str(item["sex"])
        wear_url = c_dict.get(key)
        attire_id = db.home.homepage_attire_detail.create(
            part_id=item["part_id"],
            name=item["attire_name"],
            icon_url=item["icon_url"],
            wear_url=wear_url,
            status=1,
            price=0,
            position=0,
            sequence=0,
            type=1,
            add_time=int(time.time())
        )
        box_type = int(item["part_id"])
        name = reword_name.get(box_type)
        db.tournament.user_sign_reword.create(
            sex=int(item["sex"]),
            count=attire_id,
            type=2,
            name=name,
            week=0
        )
