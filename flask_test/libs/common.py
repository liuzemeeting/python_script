import datetime
import time
import re


def from_unixtime(stamp):
    """
    时间戳转Datetime
    :param stamp: 时间
    :return: datatime
    """
    if not isinstance(stamp, int):
        return stamp
    st = time.localtime(stamp)
    return datetime.datetime(*st[:6])


def date_to_unix(obj_value, add=0):
    """
    功能: 把时间字符串转换为时间戳并返回
    ---------------------------------
    接收参数类型: '20180326', '2018-03-26', '2018-03-26 18:00:00', datetime.datetime格式
    """

    if isinstance(obj_value, datetime.datetime) or isinstance(obj_value, str) or isinstance(obj_value, unicode):
        if isinstance(obj_value, datetime.datetime):
            if add > 0:
                obj_value += datetime.timedelta(days=add)
            time_stamp = int(time.mktime(obj_value.timetuple()))
        else:
            # 只获取字符串中的数字
            string_obj = ""
            for st in re.findall(r'\d', obj_value):
                string_obj += st
            if len(string_obj) < 8:
                raise ValueError("illegal param")
            y, m, d = string_obj[:4], string_obj[4:6], string_obj[6:8]
            t_date = datetime.date(int(y), int(m), int(d))
            if add > 0:
                t_date += datetime.timedelta(days=add)
            time_stamp = int(time.mktime(t_date.timetuple()))
        return time_stamp
    else:
        raise ValueError("param type must be str or datetime.datetime")
