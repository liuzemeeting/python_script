from common import db


def get_message_id():
    """
    获取当天数学作业的user_id
    :return:
    """
    sql = """SELECT message_id from summer_resource where begin_date=1563984000 and sid=21 and type=2"""
    message_data = db.activity.fetchall_dict(sql)
    print("message_data", message_data)
    message_list = [str(obj.message_id) for obj in message_data]
    message_ids = ','.join(message_list)
    user_sql = """select user_id, test_date from sx_task_test_detail where message_id in (%s)""" % message_ids
    user_data = db.task.fetchall_dict(user_sql)
    print(user_data)
    user_list = [obj.user_id for obj in user_data]
    test_time = {obj.user_id: obj.test_date for obj in user_data}
    for i in user_list:
        add_date = test_time.get(i, 1564023600)
        add_time = max(add_date, 1564023600)
        data = db.activity.summer_mission.filter(user_id=i, add_date__gte=1563984000, type=2)[:]
        print("data", data)
        if not data:
            a = db.activity.summer_mission.create(user_id=i, add_date=add_time, type=2)
            print("a", a)


if __name__ == "__main__":
    get_message_id()
