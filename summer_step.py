from common import db
import logging, time, os

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
    user_sql = """select distinct user_id, test_date  from sx_task_test_detail 
    where add_date BETWEEN 1563984000 and 1564026000 and message_id in (%s)""" % message_ids
    user_data = db.task.fetchall_dict(user_sql)
    # print(user_data)
    user_list = [obj.user_id for obj in user_data]
    test_time = {obj.user_id: obj.test_date for obj in user_data}
    for i in user_list:
        add_date = test_time.get(i, 1564023600)
        add_time = max(add_date, 1564023600)
        data = db.activity.summer_user_info.select("step").get(user_id=i)
        step = 1
        if data:
            step = data.step
        db.activity.summer_user_info.filter(user_id=i).update(step=step)
        a = add_tea_score(i, add_time)
        print("user_id", a)
        logger.info({"user_id": i, "result": step})


def add_tea_score(user_id, add_time):
    """
    给教师加积分
    :param user_id:
    :return:
    """
    unit_class_data = db.base.mobile_order_region.select("unit_class_id", "grade_id").get(user_id=user_id)
    if not unit_class_data:
        return 0
    tea_data = db.base.mobile_order_region.select("user_id") \
        .get(unit_class_id=unit_class_data["unit_class_id"], sid=21, user_type=3)
    grade_id = unit_class_data.grade_id
    class_id = unit_class_data.unit_class_id
    if not tea_data:
        return 0
    tea_id = tea_data.user_id
    stu_and_tea_book = db.default.summer_user_book.select("book_version").filter(
        user_id__in=[user_id, tea_id], grade_id=grade_id, sid=21)[:]
    if len(stu_and_tea_book) < 2 or stu_and_tea_book[0]["book_version"] != stu_and_tea_book[1]["book_version"]:
        return 0
    open_status = db.base.mobile_subject.select("id").get(subject_id=2, user_id=user_id, status__in=(2, 3, 9))

    if open_status:
        score = 2
    else:
        score = 1
    db.default.summer_score_detail.create(
        user_id=tea_id,
        class_id=class_id,
        stu_id=user_id,
        sid=21,
        message_id=0,
        type=2,
        score=score,
        add_date=add_time
    )
    return 1


if __name__ == "__main__":
    if not os.path.exists("./xx_log/"):
        os.makedirs("./xx_log/")
    tim = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
    LOG_FILE = "./xx_log/" + str(tim)
    formatter = logging.Formatter('[%(asctime)s][%(filename)s][line: %(lineno)d][%(levelname)s] : %(message)s')
    logger = logging.getLogger('myloger')
    fh = logging.FileHandler(LOG_FILE, encoding='utf-8')  # 写入日志
    now = int(time.time())
    sh = logging.StreamHandler()  # 控制台
    fh.setLevel(logging.INFO)
    sh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(sh)
    logger.setLevel(logging.DEBUG)

    logger.info('Staring...')
    get_message_id()
