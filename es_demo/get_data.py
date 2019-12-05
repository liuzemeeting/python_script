from sql_common import db


def get_room_data():
    """
    获取房间数据
    :param request:
    :return:
    """
    sql = """
        SELECT
            ap.apartno,
            ap.apartname,
            ap.apartdesc,
            rm.roomno,
            rm.`name` room_name,
            rm.area
        FROM
            A_apart ap
            INNER JOIN A_room rm ON ap.apartno = rm.apartno
    """
    data = db.default.fetchall_dict(sql)
    print("data", data)
    data_list = [obj.apartno for obj in data]
    data_list.sort()
    apart_data = []
    for i in data_list:
        value = []
        for item in data:
            if i == item["apartno"]:
                value.append(item)
        apart = {}
        rooms = []
        door_dict = {}
        toliet = []
        cook_room = []
        for item in value:
            # print(item)
            if item.room_name in ["主卧", "次卧", "儿童房", "大次卧", "客厅"]:
                room = {}
                room["area"] = item.area
                # room["door"] = get_door_data(item.roomno)
                rooms.append(room)
            if item.room_name in ["卫生间"]:
                tlt = {}
                tlt["area"] = item.area
                # tlt["door"] = get_door_data(item.roomno)
                toliet.append(tlt)
            if item.room_name in ["厨房"]:
                ck = {}
                ck["area"] = item.area
                # ck["door"] = get_door_data(item.roomno)
                cook_room.append(ck)
        apart["rooms"] = rooms
        apart["cook_room"] = cook_room
        apart["toliet"] = toliet
        d = {i: apart}
        print(d)
        apart_data.append(d)

    print(apart_data)


def get_door_data(roomno):
    """
    获取房间内门的数据
    :param roomno:
    :return:
    """
    sql = """select doorno, roomno, width, height from A_door where roomno = %s""" % roomno
    data = db.default.fetchall_dict(sql)
    if data:
        return data
    return []


def get_window_data(roomno):
    """
    获取房间内窗户的数据
    :param roomno:
    :return:
    """
    sql = """select doorno, roomno, width, height from A_door where roomno = %s""" % roomno
    data = db.default.fetchall_dict(sql)
    if data:
        return data
    return []


if __name__ == '__main__':
    get_room_data()
