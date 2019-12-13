from es_demo.common import ElasticSearchClass
from sql_common import db
import operator

obj = ElasticSearchClass("192.168.99.107", "9200", "", "")


def compare(apartment):
    """
    将数据与规范数据对比
    :param apartment:
    :return:
    """
    rules = []
    response = obj.searchindex(index="apartment")
    rule_data = response["hits"]["hits"][0]["_source"]["any"]["body"]
    height_data = rule_data["height"]
    apart_wrong_data = []
    door_list = []
    for item in apartment:
        apart_wrong = {}
        if item["height"] != height_data["heigh"]:
            apart_wrong["apart_id"] = item["apart_id"]
            rules.append(height_data["rule"])
        rooms_data = rule_data["rooms"]
        room_ids = []
        for i in item["rooms"]:
            min_dict = {}
            print("i", i)
            for m in rooms_data["room"]:
                if i["area"] > m["area"]["area"] or i["area"] == m["area"]["area"]:
                    area_distince = i["area"] - m["area"]["area"]
                    min_dict.update({area_distince: m})
            else:
                room_ids.append(i["roomno"])
                rules.append(rooms_data["rule"])
            if min_dict:
                c = list(min_dict.keys())
                min_index = min(enumerate(c), key=operator.itemgetter(1))
                room_rule_data = min_dict.get(min_index[1])
                if i["area"] < room_rule_data["area"]["area"]:
                    room_ids.append(i["roomno"])
                    rules.append(room_rule_data["area"]["rule"])
                if i["min_height"] < room_rule_data["height"]["height"]:
                    room_ids.append(i["roomno"])
                    rules.append(room_rule_data["height"]["rule"])
                if i["min_part_height"] < room_rule_data["min_part_height"]["min_part_height"]:
                    room_ids.append(i["roomno"])
                    rules.append(room_rule_data["min_part_height"]["rule"])
                if i["min_part_area"] < room_rule_data["min_part_area"]["min_part_area"]:
                    room_ids.append(i["roomno"])
                    rules.append(room_rule_data["min_part_area"]["rule"])

                door_ids = []
                for k in i["door"]:
                    if k["height"] < room_rule_data["door"]["height"]\
                            and k["width"] >= room_rule_data["door"]["width"]:
                        door_ids.append(k["doorno"])
                        rules.append(room_rule_data["min_part_area"]["rule"])
                door_data = {"room_id": i["roomno"], "door_ids": door_ids}
                door_list.append(door_data)
        apart_wrong["room_data"] = room_ids
        apart_wrong["door_data"] = door_list
        # 检测卫生间规范
        toliet_rule_data = rule_data["toliets"]
        for m in item["toliet"]:
            t_rule_data = {}
            for item in toliet_rule_data["toliet"]:
                if m["bianqi"] == item["bianqi"] and m["xiyuqi"] == item["xiyuqi"] \
                        and m["ximianqi"] == item["ximianqi"] and m["xiyiji"] == item["xiyiji"]:
                    t_rule_data = item
            else:
                rules.append(toliet_rule_data["rule"])
            if t_rule_data:
                if m["height"] < t_rule_data["height"]["height"]:
                    room_ids.append(i["roomno"])
                    rules.append(t_rule_data["height"]["rule"])
                if m["water_distince"] < t_rule_data["water_distince"]["water_distince"]:
                    room_ids.append(i["roomno"])
                    rules.append(t_rule_data["water_distince"]["rule"])
                if m["area"] < t_rule_data["area"]["area"]:
                    room_ids.append(i["roomno"])
                    rules.append(t_rule_data["area"]["rule"])
                else:
                    m["area"] = {"area": m["area"], "status": 0}
                if m["door"]["height"] < t_rule_data["door"]["height"] or m["door"]["width"] < t_rule_data["door"]["width"]:
                    room_ids.append(i["roomno"])
                    rules.append(t_rule_data["door"]["rule"])
                if m["door"]["width"] < t_rule_data["door"]["width"]:
                    room_ids.append(i["roomno"])
                    rules.append(t_rule_data["door"]["rule"])
        else:
            print("ffffffffffffffff")
        # 检测厨房规范
        c_rule_data = []
        for i in item["cook_room"]:
            min_dict = {}
            for item in rule_data["cook_rooms"]["cook_room"]:
                if i["area"] >= item["area"]["area"]:
                    area_distince = i["area"] - item["area"]["area"]
                    min_dict.update({area_distince: item})
            else:
                i["status"] = 1
                rules.append(rule_data["cook_rooms"]["rule"])
            if min_dict:
                i["status"] = 0
                c = list(min_dict.keys())
                min_index = min(enumerate(c), key=operator.itemgetter(1))
                cook_rule_data = min_dict.get(min_index[1])
                if i["water_distince"] >= cook_rule_data["water_distince"]["water_distince"]:
                    i["water_distince"] = {"water_distince": i["water_distince"], "status": 0}
                else:
                    i["water_distince"] = {"water_distince": i["water_distince"], "status": 1}
                if i["door"]["height"] < cook_rule_data["door"]["height"] and i["door"]["width"] < cook_rule_data["door"]["width"]:
                    i["door"].update({"status": 0})
                else:
                    i["door"].update({"status": 1})
        apart_wrong_data.append(apart_wrong)
    print("apart_wrong_data", apart_wrong_data)
    print(rules)





