from es_demo.common import ElasticSearchClass
from common import db
import operator
from datetime import datetime

obj = ElasticSearchClass("192.168.99.107", "9200", "", "")


if __name__ == "__main__":

    # response = obj.searchindex(index="apartment")
    # print("response", response)
    # print(response["hits"]["hits"][0]["_source"]["any"]["body"])

    # # body = {
    # #     "query": {
    # #         "match_all": {
    # #             # "name": "一室一厅一厨一卫"
    # #         }
    # #     }
    # # }


    apartment = {
        "name": "室内户型",
        "height": 2.70,
        "rooms": [{
            "name": "卧室",
            "area": 9,
            "door": {
                "height": 1.95,
                "width": 0.86,
            },
            "height": 2.40,
            "min_part_height": 2.10,
            "min_part_area": 0.33,
        },
            {
                "name": "卧室",
                "area": 9,
                "door": {
                    "height": 1.95,
                    "width": 0.86,
                },
                "height": 2.40,
                "min_part_height": 2.10,
                "min_part_area": 0.33,
            }
        ],
        "cook_room": [{
            "name": "厨房",
            "water_distince": 1.80,
            "door": {
                "height": 1.96,
                "width": 0.80,
            },
            "area": 3.8,
        },
            {
                "name": "厨房",
                "water_distince": 1.80,
                "door": {
                    "height": 1.96,
                    "width": 0.80,
                },
                "area": 3.8,
            }
        ],
        "toliet": [{
            "name": "卫生间",
            "height": 2.10,
            "area": 2.4,
            "door": {
                "height": 2.00,
                "width": 0.70,
            },
            "water_distince": 1.80,
            "bianqi": 1,
            "xiyuqi": 1,
            "ximianqi": 0,
            "xiyiji": 0,
        }]
    }
    body = {
        "query": {
            "match": {
                "any.body.name.keyword": "户型"
            }
        }
    }
    rules = []
    response = obj.search(index="apartment", body=body)
    rule_data = response["hits"]["hits"][0]["_source"]["any"]["body"]
    height_data = rule_data["height"]
    if apartment["height"] != height_data["heigh"]:
        apartment["height"] = {"height": apartment["height"], "status": 1}
        rules.append(height_data["rule"])
    rooms_data = rule_data["rooms"]
    for i in apartment["rooms"]:
        min_dict = {}
        for item in rule_data["rooms"]["room"]:
            if i["area"] > item["area"]["area"] or i["area"] == item["area"]["area"]:
                area_distince = i["area"] - item["area"]["area"]
                min_dict.update({area_distince: item})
        else:
            i["status"] = 1
            rules.append(rule_data["rooms"]["rule"])
        if min_dict:
            i["status"] = 0
            c = list(min_dict.keys())
            min_index = min(enumerate(c), key=operator.itemgetter(1))
            room_rule_data = min_dict.get(min_index[1])
            if i["area"] >= room_rule_data["area"]["area"]:
                i["area"] = {"area": i["area"], "status": 0}
            else:
                i["area"] = {"area": i["area"], "status": 1}
                rules.append(room_rule_data["area"]["rule"])
            if i["height"] >= room_rule_data["height"]["height"]:
                i["height"] = {"height": i["height"], "status": 0}
            else:
                i["height"] = {"height": i["height"], "status": 1}
                rules.append(room_rule_data["height"]["rule"])
            if i["min_part_height"] >= room_rule_data["min_part_height"]["min_part_height"]:
                i["min_part_height"] = {"min_part_height": i["min_part_height"], "status": 0}
            else:
                i["min_part_height"] = {"min_part_height": i["min_part_height"], "status": 1}
                rules.append(room_rule_data["min_part_height"]["rule"])
            if i["min_part_area"] >= room_rule_data["min_part_area"]["min_part_area"]:
                i["min_part_area"] = {"min_part_area": i["min_part_area"], "status": 0}
            else:
                i["min_part_area"] = {"min_part_area": i["min_part_area"], "status": 1}
                rules.append(room_rule_data["min_part_area"]["rule"])
            if i["door"]["height"] >= room_rule_data["door"]["height"]\
                    and i["door"]["width"] >= room_rule_data["door"]["width"]:
                i["door"]["status"] = 0
            else:
                i["door"]["status"] = 1
                rules.append(room_rule_data["min_part_area"]["rule"])
    # 检测卫生间规范
    toliet_rule_data = rule_data["toliets"]
    for m in apartment["toliet"]:
        t_rule_data = {}
        for item in toliet_rule_data["toliet"]:
            if m["bianqi"] == item["bianqi"] and m["xiyuqi"] == item["xiyuqi"] \
                    and m["ximianqi"] == item["ximianqi"] and m["xiyiji"] == item["xiyiji"]:
                t_rule_data = item
        else:
            rules.append(toliet_rule_data["rule"])
        if t_rule_data:
            if m["height"] < t_rule_data["height"]["height"]:
                m["height"] = {"height": m["height"], "status": 1}
                rules.append(t_rule_data["height"]["rule"])
            else:
                m["height"] = {"height": m["height"], "status": 0}
            if m["water_distince"] < t_rule_data["water_distince"]["water_distince"]:
                m["water_distince"] = {"water_distince": m["water_distince"], "status": 1}
                rules.append(t_rule_data["water_distince"]["rule"])
            else:
                m["water_distince"] = {"water_distince": m["water_distince"], "status": 0}
            if m["area"] < t_rule_data["area"]["area"]:
                m["area"] = {"area": m["area"], "status": 1}
                rules.append(t_rule_data["area"]["rule"])
            else:
                m["area"] = {"area": m["area"], "status": 0}
            if m["door"]["height"] >= t_rule_data["door"]["height"] and m["door"]["width"] >= t_rule_data["door"]["width"]:
                m["door"]["status"] = 0
            else:
                m["door"]["status"] = 1
                rules.append(t_rule_data["door"]["rule"])
            if m["door"]["width"] < t_rule_data["door"]["width"]:
                m["door"]["width"] = {"width": m["door"]["width"], "status": 1}
                rules.append(t_rule_data["door"]["rule"])
            else:
                m["door"]["width"] = {"width": m["door"]["width"], "status": 0}
    # 检测厨房规范
    c_rule_data = []
    for i in apartment["cook_room"]:
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
                print("i", i)
                i["water_distince"] = {"water_distince": i["water_distince"], "status": 1}
            if i["door"]["height"] >= cook_rule_data["door"]["height"] and i["door"]["width"] >= cook_rule_data["door"]["width"]:
                i["door"].update({"status": 0})
            else:
                i["door"].update({"status": 1})
    print(rules)
    print("apartment", apartment)

    # 户外





