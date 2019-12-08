from common import db


data = [{"id": 1, "pid": 0, "name": " 超级管理组"},
{"id": 2, "pid": 1, "name": "麦莎国际"},
{"id": 7, "pid": 2, "name": "王者队"},
{"id": 16, "pid": 7, "name": "王者队员工"},
{"id": 9, "pid": 2, "name": "疯狂队"},
{"id": 17, "pid": 9, "name": "疯狂队员工"},
{"id": 10, "pid": 2, "name": "牛人队"},
{"id": 18, "pid": 10, "name": "牛人队员工"},
{"id": 11, "pid": 2, "name": "爆单队"},
{"id": 19, "pid": 11, "name": "爆单队员工"},
{"id": 12, "pid": 2, "name": "亮剑队"},
{"id": 20, "pid": 12, "name": "亮剑队员工"},
{"id": 13, "pid": 2, "name": "梦想队"},
{"id": 21, "pid": 13, "name": "高潮锋"},
{"id": 14, "pid": 2, "name": "荣耀队"},
{"id": 22, "pid": 14, "name": "荣耀队员工"},
{"id": 68, "pid": 2, "name": "刘帅组"},
{"id": 69, "pid": 68, "name": "赵培"},
{"id": 77, "pid": 69, "name": "赵培员工"},
{"id": 76, "pid": 68, "name": "王鹏"},
{"id": 78, "pid": 76, "name": "王鹏组员工"},
{"id": 107, "pid": 2, "name": "培训组"},
{"id": 4, "pid": 1, "name": "遵古"},
{"id": 27, "pid": 4, "name": "孙龙"},
{"id": 28, "pid": 27, "name": "孙龙专员"},
{"id": 29, "pid": 4, "name": "美玲"},
{"id": 30, "pid": 29, "name": "美玲专员"},
{"id": 31, "pid": 4, "name": "董灵"},
{"id": 32, "pid": 31, "name": "董灵专员"},
{"id": 34, "pid": 4, "name": "遵商"},
{"id": 71, "pid": 34, "name": "遵商专员"},
{"id": 36, "pid": 4, "name": "牛阳"},
{"id": 53, "pid": 36, "name": "牛阳专员"},
{"id": 38, "pid": 4, "name": "卢刚刚"},
{"id": 64, "pid": 38, "name": "卢刚刚专员"},
{"id": 103, "pid": 64, "name": "1"},
{"id": 42, "pid": 4, "name": "申红梅"},
{"id": 59, "pid": 42, "name": "杨超专员"},
{"id": 44, "pid": 4, "name": "贤霖电商"},
{"id": 57, "pid": 44, "name": "白玉专员"},
{"id": 46, "pid": 4, "name": "腾茂电商"},
{"id": 60, "pid": 46, "name": "腾茂电商专员"},
{"id": 54, "pid": 4, "name": "成鹏举"},
{"id": 56, "pid": 54, "name": "成鹏举专员"},
{"id": 65, "pid": 4, "name": "郭鑫"},
{"id": 66, "pid": 65, "name": "郭鑫专员"},
{"id": 70, "pid": 4, "name": "李总"},
{"id": 72, "pid": 4, "name": "安阳付总"},
{"id": 73, "pid": 72, "name": "付军专员"},
{"id": 100, "pid": 4, "name": "阿豫"},
{"id": 101, "pid": 100, "name": "阿豫专员"},
{"id": 33, "pid": 1, "name": "遵古联盟"},
{"id": 74, "pid": 1, "name": "爆单单联盟"},
{"id": 84, "pid": 74, "name": "无敌队"},
{"id": 85, "pid": 84, "name": "无敌队员工"},
{"id": 86, "pid": 74, "name": "爆单队"},
{"id": 87, "pid": 86, "name": "爆单队员工"},
{"id": 88, "pid": 74, "name": "黑马队"},
{"id": 89, "pid": 88, "name": "黑马队员工"},
{"id": 90, "pid": 74, "name": "突击队"},
{"id": 91, "pid": 90, "name": "突击队员工"},
{"id": 98, "pid": 74, "name": "淘宝队"},
{"id": 99, "pid": 98, "name": "淘宝对员工"},
{"id": 111, "pid": 74, "name": "梦之队"},
{"id": 112, "pid": 74, "name": "梦之队员工"},
{"id": 79, "pid": 1, "name": "伟业联盟"},
{"id": 80, "pid": 79, "name": "主管"},
{"id": 81, "pid": 80, "name": "员工"},
{"id": 93, "pid": 1, "name": "挺起青龙"},
{"id": 94, "pid": 93, "name": "销售一部"},
{"id": 95, "pid": 94, "name": "一部员工"},
{"id": 96, "pid": 93, "name": "销售二部"},
{"id": 97, "pid": 96, "name": "二部员工"},
{"id": 104, "pid": 1, "name": "熊大军团"},
{"id": 105, "pid": 104, "name": "1队"},
{"id": 106, "pid": 105, "name": "1队员工"},
{"id": 108, "pid": 104, "name": "2队"},
{"id": 109, "pid": 104, "name": "2队员工"}]
if __name__ == '__main__':
    # data_dict = {obj["id"]: obj for obj in data}
    # data_ids = list(data_dict.keys())
    # data_ids.sort()
    # data_list = []
    # for i in data_ids:
    #     p_data = data_dict.get(i)
    #     pid = p_data["pid"]
    #     name = p_data["name"]
    #     d = {
    #         "id": i,
    #         "pid": pid,
    #         "name": name
    #     }
    #     data_list.append(d)
    # db.default.system_group.bulk_create(data_list, ignore=True)
    sql = """select * from system_group"""
    data = db.default.fetchall_dict(sql)

    data_list = []
    for i in data:
        pass


def foo(item, data):
    pass