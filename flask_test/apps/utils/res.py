# !/usr/bin/python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 11:11
# @Author  : hshen
import datetime
from flask import jsonify
from .db import CRUDMixin, model_to_dict


class ResCode(object):
    """返回代码"""
    # 自定义请求成功代码
    RES_OK = 200
    # 自定义请求失败代码
    RES_FALSE = 401
    # 请求成功返回信息
    MESSAGE_OK = u'请求成功'
    # 请求失败返回信息
    MESSAGE_FALSE = u'请求失败'


def json_response(code=ResCode.RES_OK, msg=u"", data=None, select_cols=[]):
    """
    说明：请求响应json数据
    ----------------------------------------
    修改人          修改日期          修改原因
    ----------------------------------------
    Zuyong Du         2018-10-22
    ----------------------------------------
    :param code: http，返回代码，默认为 200成功
    :param msg: 返回消息，默认为'成功'
    :param data:    返回的数据列表，必须是可以iterator，比如dict,list,tuple都可以
    :return json:   返回json对象
    """
    result = {"status": str(code), "message": msg, "data":""}
    if data:
        # 判断是否是数据模型类型，假如是，则进行to_dict()转换
        if isinstance(data, CRUDMixin) and isinstance(data, list) is False:
            result['data'] = model_to_dict(data)
            # result['data'] = data.to_json()
        elif isinstance(data, list) and isinstance(data[0], CRUDMixin):
            # result['data'] = map(lambda v: model_to_dict(v), data)
            ll = list()
            for row in data:
                ll.append(model_to_dict(row))
                # ll.append(row.to_json())
            result['data'] = ll
        elif isinstance(data, list) and select_cols:
            result['data'] = format_orm_result(data, select_cols)
        else:
            result['data'] = data
    else:
        result['data'] = data
    return jsonify(result)


def format_orm_result(result, select_cols_):
    """
    格式化sqlalchemy查询结果
    :param result:
    :param select_cols_:
    :return:
    """
    data = []
    if isinstance(result, list):
        for item in result:
            data.append({name.key: item[index]
                         for index, name in enumerate(select_cols_)})
    else:
        data.append({name.key: result[index]
                     for index, name in enumerate(select_cols_)})
    return data