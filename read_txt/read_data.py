import re
import redis
from common import db

if __name__ == "__main__":
    # f = open("building.txt", "r", encoding="utf-8")
    # data = f.readlines()
    # data_total = []
    # for i in data:
    #     print(i.split("|"))
    #     data_list = i.split("|")
    #     item_id = data_list[0]
    #     item_coutent = data_list[1].replace("\n", "")
    #     d = {
    #         "artical_id": item_id,
    #         "artical_content": item_coutent
    #     }
    #     data_total.append(d)
    # db.default.build_artical.bulk_create(data_total, ignore=True)
    a = []
    for i in a:
        print("ddddddddddd")
    else:
        print("dssssssssssssssssss")

    a = {1:3, 8:7, 2:3,6:7,4:0, 0:1}
    b = list(a.keys())
    import operator
    min_index = min(enumerate(b), key=operator.itemgetter(1))
    print(min_index)