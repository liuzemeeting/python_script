import re
import redis
from common import db

if __name__ == "__main__":
    f = open("test.txt", "r", encoding="gbk")
    data = f.readlines()
    data_total = []
    data_list =[]
    for i in data:
        print(i.strip())
        column_data = re.findall('catSelect(.*),', i)
        item_id = column_data[0].replace("(", "")
        print("column_data", column_data[0].replace("(", ""))
        item_data = re.findall('>(.*)</span></a>', i)
        print("item_data", item_data[0].split(">")[1])
        item_name = item_data[0].split(">")[1]
        dict = {"item_id": item_id, "item_name": item_name}
        data_list.append(dict)
    #     data_list = i.split("|")
    #     item_id = data_list[0]
    #     item_coutent = data_list[1].replace("\n", "")
    #     d = {
    #         "artical_id": item_id,
    #         "artical_content": item_coutent
    #     }
    #     data_total.append(d)
    db.default.good_type.bulk_create(data_list, ignore=True)
    # a = []
    # for i in a:
    #     print("ddddddddddd")
    # else:
    #     print("dssssssssssssssssss")
    #
    # a = {1:3, 8:7, 2:3,6:7,4:0, 0:1}
    # b = list(a.keys())
    # import operator
    # min_index = min(enumerate(b), key=operator.itemgetter(1))
    # print(min_index)