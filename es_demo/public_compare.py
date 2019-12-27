from es_demo.common import ElasticSearchClass
from sql_common import db
import operator

obj = ElasticSearchClass("192.168.99.107", "9200", "", "")


class public_Compare:

    def __init__(self, index_name):
        self.index_name = index_name
        response = obj.searchindex(index=index_name)
        rule_data = response["hits"]["hits"][0]["_source"]["any"]["body"]
        self.rule_data = rule_data

    def compare_loft(self):
        loft_data = self.rule_data["loft"]
        # print(loft_data)

    def compare_stair(self):
        stair_data = self.rule_data["stair"]
        print(stair_data)

    def compare_exit(self, exit_data):
        rule_exit_data = self.rule_data["safe_exit"]
        rules = []
        exit_ids = []
        for item in exit_data:
            if item["floor"] > 18:
                floor = 19
            if item["floor"] >= 10:
                floor = 18
            if item["floor"] < 10:
                floor = 10
            rule_floor = rule_exit_data["outside"].get(str(floor))
            flag = True
            if item["build_area"] < rule_floor["bulid_area"] or item["build_area"] < rule_floor["bulid_area"] \
                    or item["build_area"] < rule_floor["bulid_area"]:
                flag = False
                rules.append(rule_floor["floor"])
            if item["distince"] < rule_exit_data["safe_out_distince"]["safe_out_distince"]:
                flag = False
                rules.append(rule_exit_data["safe_out_distince"]["rule"])
            if item["toword_sparse"] != rule_exit_data["stairs_anterroom_door_safe"]["status"]:
                flag = False
                rules.append(rule_exit_data["stairs_anterroom_door_safe"]["rule"])
            if flag == False:
                exit_ids.append(item["id"])
        print(exit_ids, rules)

    def room_compare(self, room_data):
        """
        房间数据对比
        :return:
        """
        rule_room_data = self.rule_data["rooms"]
        rules = []
        room_ids = []
        for i in room_data:
            min_dict = {}
            print("i", i)
            for m in rule_room_data:
                if i["area"] > m["area"]["area"] or i["area"] == m["area"]["area"]:
                    area_distince = i["area"] - m["area"]["area"]
                    min_dict.update({area_distince: m})
            else:
                room_ids.append(i["roomno"])
                rules.append(rule_room_data)
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

    def cook_room_compare(self):
        """
        厨房数据对比
        :return:
        """
        pass

    def toilent_compare(self):
        """
        卫生间数据对比
        :return:
        """
        pass