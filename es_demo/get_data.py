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
            rm.area,
            dr.roomno dr_roomno,
            dr.`name` door_name,
            dr.weigth door_weight,
            dr.height  door height
        FROM
            A_apart ap
            INNER JOIN A_room rm ON ap.apartno = rm.apartno
            INNER JOIN A_door dr ON dr.roomno = rm.roomno
    """
    data = db.default.fetchall_dict(sql)
    data_list = [obj.apartno for obj in data]
    data_list.sort()
    apart_data = []
    for i in data_list:
        value = []
        for item in data:
            if i == item["apartno"]:
                value.append(item)
        # d = {i: value}
        # apart_data.append(d)
        rooms = []
        for item in value:
            if item.room_name in ["主卧", "次卧", "儿童房", "大次卧", "客厅"]:
                room = {}
                door = []
                room["area"] = item.area
                room["door"] = {
                    "height": item.door_height,
                    "width": item.door_weigth
                }
                rooms.append(room)
            if item.room_name in []:
                pass

    print(apart_data)


if __name__ == '__main__':
    get_room_data()
