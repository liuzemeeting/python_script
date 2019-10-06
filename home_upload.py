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
    for root, dirs, files in os.walk('box_bg'):
        for i in files:
            files = {"field1": open(f"{root}/{i}", 'rb')}
            r = requests.post(url, files=files)
            response = json.loads(r.text.replace('\'', '"'))[0]
            file_name = response["file_name"]
            file_url = response["file_url"]
            name = file_name.split('.')[0]
            all_name = name.split('-')
            part_id = all_name[1]
            sid = all_name[2]
            sex = all_name[3]
            d = {
                "attire_name": name,
                "part_id": part_id,
                "sid": sid,
                "sex": sex,
                "icon_url": file_url
            }
            icon_data.append(d)
    for root, dirs, files in os.walk('box_tc'):
        for i in files:
            files = {"field1": open(f"{root}/{i}", 'rb')}
            r = requests.post(url, files=files)
            response = json.loads(r.text.replace('\'', '"'))[0]
            file_name = response["file_name"]
            file_url = response["file_url"]
            name = file_name.split('.')[0]
            all_name = name.split('-')
            part_id = all_name[1]
            sid = all_name[2]
            sex = all_name[3]
            d = {
                "part_id": part_id,
                "sid": sid,
                "sex": sex,
                "file_url": file_url
            }
            attire_data.append(d)
    return icon_data, attire_data


if __name__ == '__main__':
    icon_data, attire_data = upload()
    reword_name = {2: "发饰", 3: "上衣", 4: "下衣", 5: "鞋子", 6: "场景"}
    reword_girl_name = {8: "发饰", 9: "上衣", 10: "下衣", 11: "鞋子", 12: "场景"}
    c_dict = {}
    for i in attire_data:
        key = str(i["part_id"]) + str(i["sid"]) + str(i["sex"])
        if key in c_dict:
            b = c_dict["%s"%key]
            attire_fair = i["file_url"]
            b += ",%s" % attire_fair
            c_dict["%s"%key] = b
        else:
            c_dict.update({key: i["file_url"]})
    for item in icon_data:
        key = str(item["part_id"]) + str(item["sid"]) + str(item["sex"])
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
        box_type = int(item["part_id"]) + 1
        name = reword_name.get(box_type)
        if int(item["sex"]) == 2:
            name = reword_girl_name.get(int(item["part_id"]))
            box_type = int(item["part_id"]) - 6
        db.tournament.user_box_res.create(
            sid=int(item["sid"]),
            sex=int(item["sex"]),
            count=attire_id,
            type=box_type,
            name=name
        )
