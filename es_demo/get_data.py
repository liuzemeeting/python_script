from sql_common import db
from es_demo.compare import compare


def get_room_data():
    """
    获取房间数据
    :param request:
    :return:
    """
    sql = """
        SELECT
            ap.apartno,
            ap.height ap_height,
            ap.apartname,
            ap.apartdesc,
            rm.id roomno,
            rm.`name` room_name,
            rm.area,
            rm.min_part_area,
            rm.min_height,
            rm.min_part_height,
            rm.bianqi,
            rm.xiyuqi,
            rm.ximianqi,
            rm.water_distince
        FROM
            B_apart ap
            INNER JOIN B_room rm ON ap.apartno = rm.apart_id
    """
    data = db.default.fetchall_dict(sql)
    data_list = list(set([obj.apartno for obj in data]))
    apart_data = []
    for i in data_list:
        value = []
        for item in data:
            if i == item["apartno"]:
                value.append(item)
        apart = {}
        apart["apart_id"] = i
        rooms = []
        door_dict = {}
        toliet = []
        cook_room = []
        for item in value:
            apart["height"] = item.ap_height
            if item.room_name in ["主卧", "次卧", "儿童房", "大次卧", "客厅", "主卧室"]:
                room = {}
                room["roomno"] = item.roomno
                room["min_height"] = item.min_height
                room["min_part_height"] = item.min_part_height
                room["area"] = item.area
                room["min_part_area"] = item.min_part_area
                room["door"] = get_door_data(item.roomno)
                rooms.append(room)
            if item.room_name in ["卫生间"]:
                tlt = {}
                tlt["roomno"] = item.roomno
                tlt["min_height"] = item.min_height
                tlt["height"] = item.min_height
                tlt["water_distince"] = item.water_distince
                tlt["min_part_height"] = item.min_part_height
                tlt["area"] = item.area
                tlt["min_part_area"] = item.min_part_area
                # tlt["door"] = get_door_data(item.roomno)
                tlt["bianqi"] = item.bianqi
                tlt["xiyuqi"] = item.xiyuqi
                tlt["ximianqi"] = item.ximianqi
                toliet.append(tlt)
            if item.room_name in ["厨房"]:
                ck = {}
                ck["area"] = item.area
                # ck["door"] = get_door_data(item.roomno)
                cook_room.append(ck)
        apart["rooms"] = rooms
        apart["cook_room"] = cook_room
        apart["toliet"] = toliet
        apart_data.append(apart)
    print("apart_data", apart_data)
    compare(apart_data)


def get_door_data(roomno):
    """
    获取房间内门的数据
    :param roomno:
    :return:
    """
    sql = """select id doorno, room_id, width, height from B_door where room_id = %s""" % roomno
    data = db.default.fetchall_dict(sql)
    print("data", data)
    if data:
        return data
    return []


def get_window_data(roomno):
    """
    获取房间内窗户的数据
    :param roomno:
    :return:
    """
    sql = """select id doorno, room_id, width, height from B_door where room_id = %s""" % roomno
    data = db.default.fetchall_dict(sql)
    if data:
        return data
    return []


if __name__ == '__main__':
    get_room_data()
