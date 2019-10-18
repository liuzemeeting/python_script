# coding: utf-8
import datetime
import time

from typing import (
    Set,
    Dict,
    List,
)


# log
def log(*args, **kwargs):
    """
    说明：日志打印
    --------------------------------
    修改人    修改日期         修改原因
    --------------------------------
    王建彬    2018-10-17
    --------------------------------
    """
    format_time = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format_time, value)
    print(dt, *args, **kwargs)


class Constructor(dict):
    """
    说明：字典构造器
    --------------------------------
    修改人    修改日期         修改原因
    --------------------------------
    王建彬    2018-10-17
    --------------------------------
    Usage::
        >>> s = Constructor(name='wiki')
        >>> s.name
        'wiki'
        >>> s.age = 18
        >>> s.age
        18
        >>> s
        {'age': 18, 'name': 'wiki'}
    ------------------
    """

    def __init__(self, **kw):
        super(Constructor, self).__init__(kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Constructor' object has no attribute '{}'".format(key))

    def __setattr__(self, key, value):
        self[key] = value


def mapping_from_match(
        keys: Set,
        query_list: List[Dict],
) -> Dict:
    """
    说明：数据匹配映射到表
    --------------------------------
    修改人    修改日期         修改原因
    --------------------------------
    王建彬    2018-10-17
    --------------------------------
    """
    # 通过keys集合生成匹配映射表, 用来填充数据
    match_map = {k: {} for k in keys}

    # 依次对每个数据源匹配和更新映射表
    for query in query_list:
        for k, v in match_map.items():
            # 获取key对应的值
            r = query.get(k, {})

            # 更新到value中
            v.update(r)

            # 更新匹配映射表
            match_map[k] = v

    return match_map


def array_day_from_range(
        begin_ts: int,
        end_ts: int,
) -> List:
    """
    说明：返回格式化时间范围的列表
    --------------------------------
    修改人    修改日期         修改原因
    --------------------------------
    王建彬    2018-11-07
    --------------------------------
    """
    begin = datetime.datetime.fromtimestamp(begin_ts)
    end = datetime.datetime.fromtimestamp(end_ts)

    # 添加每天时间
    range = []

    dt = begin
    while dt <= end:
        fmt = dt.strftime("%Y%m%d")
        range.append(fmt)

        dt += datetime.timedelta(days=1)

    return range
