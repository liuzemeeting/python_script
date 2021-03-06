from sql_common import db
from es_demo.public_compare import public_Compare


def get_public():
    """
    获取公共数据
    :return:
    """
    sql = """select  id public_id from B_public where dwg_id=%s""" % 1
    public_data = db.default.fetchone_dict(sql)
    public_id = public_data.public_id
    p_compare = public_Compare("common_part")
    loft_data = get_loft_data(public_id)
    stair_data = get_stair_data(public_id)
    exit_data = get_exit_data(public_id)
    p_compare.compare_exit(exit_data)
    p_compare.compare_loft()
    p_compare.compare_stair()



def get_loft_data(public_id):
    """
    获取电梯数据
    :return:
    """
    sql = """select * from B_loft where public_id = %s""" % public_id
    loft_data = db.default.fetchall_dict(sql)
    return loft_data


def get_stair_data(public_id):
    """
    获取楼梯数据
    :return:
    """
    sql = """select * from B_loft where public_id = %s""" % public_id
    stair_data = db.default.fetchall_dict(sql)
    return stair_data


def get_exit_data(public_id):
    """
    获取安全出口数据
    :return:
    """
    sql = """select * from B_safe_exit where public_id = %s""" % public_id
    exit_data = db.default.fetchall_dict(sql)
    return exit_data


if __name__ == '__main__':
    get_public()