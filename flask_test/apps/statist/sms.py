# coding=utf-8
# @Time    : 2018/10/22 下午3:24
# @Author  : Zuyong Du
import traceback
import logging
import inspect
import datetime
from collections import Iterable
from flask_restful import Resource, reqparse
from application import db
from apps.utils.res import json_response
from libs.common import date_to_unix, from_unixtime
log = logging.getLogger(__name__)


def r_next_month(now_time):
    """
    方法功能说明:获取下个月一号日期
    -------------------------------------------------
    :param now_time datetime 类型
    :return month_time datetime 类型
    """
    next_month = now_time.month
    next_year = now_time.year
    if next_month == 12:
        next_month = 1
        next_year += 1
    else:
        next_month += 1
    month_time = datetime.datetime(year=next_year, month=next_month, day=1)
    return month_time


def get_data(db_data):
    """处理数据库查询结果"""
    result = None
    if isinstance(db_data, Iterable):
        for i in db_data:
            result = i[0]
        return result
    else:
        return 0


def execute(db_name, sql):
    try:
        result = db.get_engine(bind=db_name).execute(sql)
        return result
    except Exception as e:
        traceback.print_exc()
        log.error("%s:%s" % (inspect.stack()[0][3], e))
        result = db.get_engine(bind=db_name).execute(sql)
        return result


class SmsAPI(Resource):

    @staticmethod
    def post():
        """
        说明：短信数据分析
        可以按照最近一小时、每天、每月数据展示
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        吕建威         2018-10-23
        ----------------------------------------
        """
        parser = reqparse.RequestParser()
        # required 参数是否为必须的 True 参数必须传 False 可以不传
        parser.add_argument("data_type", required=True, help="请选择查询类型")
        parser.add_argument("begin_date")
        parser.add_argument("end_date")
        args = parser.parse_args()
        # 获取参数值
        data_type = int(args.data_type)
        begin_date = int(args.begin_date) if args.begin_date else ""
        end_date = int(args.end_date) if args.end_date else ""
        context = {}
        try:
            if end_date:
                end_date = from_unixtime(end_date)
            # 前端未传递起始和截止时间,默认开始时间为当月初,结束时间为向后推一天的时间
            if begin_date == "" and end_date == "":
                date_now = datetime.datetime.now()
                begin_date = date_now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                end_date = date_now.replace(hour=0, minute=0, second=0, microsecond=0)

                if data_type == 3:
                    # 月维度,默认起始时间为当年一月一日起
                    begin_date = begin_date.replace(month=1)
            end_date = end_date + datetime.timedelta(days=1)
            # 将开始时间和截止时间转换为数据库可接受的类型
            begin_date = from_unixtime(begin_date)
            begin_day = int("%d%.2d%.2d" % (begin_date.year, begin_date.month, begin_date.day))
            end_day = int("%d%.2d%.2d" % (end_date.year, end_date.month, end_date.day))
            # 即时一小时内数据
            if data_type == 0:
                # 结束时间为此刻的时间
                date_now = datetime.datetime.now().replace(second=0, microsecond=0)
                # 开始的时间为一个小时以前
                begin_time = date_now - datetime.timedelta(hours=1)
                # 数据结果列表
                data_list = []
                # 以五分钟为时间间隔循环查询短信发送接收情况
                while True:
                    if begin_time < date_now:
                        end_time = begin_time + datetime.timedelta(minutes=5)
                        # 时间节点段
                        date_node = "%d:%.2d" % (begin_time.hour, begin_time.minute) + '-' + "%d:%.2d" % (end_time.hour, end_time.minute)
                        # 开始截止时间戳
                        begin_unix = date_to_unix(begin_time)
                        end_unix = date_to_unix(end_time)
                        # 短信总数
                        sql_mt = """SELECT COUNT(1) FROM mobile_mt WHERE add_date BETWEEN '%s' AND '%s';""" % (begin_unix, end_unix)
                        data_mt = execute('mobile_sms', sql_mt)
                        mt_num = get_data(data_mt)
                        # 短信提交
                        sql_submit = """SELECT COUNT(1) FROM mt_submit WHERE submit_date BETWEEN '%s' AND '%s';""" % (begin_time, end_time)
                        data_submit = execute('mobile_sms', sql_submit)
                        submit_num = get_data(data_submit)
                        # 移动响应
                        sql_resp = """SELECT COUNT(1) FROM mt_resp WHERE resp_date BETWEEN '%s' AND '%s';""" % (begin_time, end_time)
                        data_resp = execute('mobile_sms', sql_resp)
                        resp_num = get_data(data_resp)
                        # 状态报告
                        sql_rep = """SELECT COUNT(1) FROM mt_report WHERE report_date BETWEEN '%s' AND '%s';""" % (begin_time, end_time)
                        data_rep = execute('mobile_sms', sql_rep)
                        rep_num = get_data(data_rep)
                        # 未提交网关
                        sql_no_submit = """SELECT COUNT(1) FROM (SELECT m.redis_id FROM mobile_mt m LEFT JOIN mt_submit s ON m.redis_id=s.redis_id 
                        WHERE m.add_date>=UNIX_TIMESTAMP('%s') AND m.add_date<UNIX_TIMESTAMP('%s') AND s.id IS NULL AND m.status<0 GROUP BY m.redis_id) AS t;
                        """ % (begin_time, end_time)
                        data_no_submit = execute('mobile_sms', sql_no_submit)
                        no_submit_num = get_data(data_no_submit)
                        # 未收到网关
                        sql_no_response = """SELECT COUNT(1) FROM (SELECT m.redis_id FROM mobile_mt m LEFT JOIN mt_resp s ON m.redis_id=s.redis_id 
                        WHERE m.add_date>=UNIX_TIMESTAMP('%s') AND m.add_date<UNIX_TIMESTAMP('%s') AND s.id IS NULL AND m.status<0 GROUP BY m.redis_id) AS t;
                        """ % (begin_time, end_time)
                        data_no_response = execute('mobile_sms', sql_no_response)
                        no_response_num = get_data(data_no_response)
                        data_dict = {"date_node": date_node, "mt": mt_num, "submit": submit_num, "resp": resp_num,
                                     "rep": rep_num, "no_submit": no_submit_num, "no_response": no_response_num}
                        data_list.append(data_dict)
                        begin_time = end_time
                    else:
                        break
                # 数据整理 符合前端 echarts 展示
                data_x = [str(obj["date_node"]) for obj in data_list if data_list]
                context["data_x"] = data_x
                data_rep = [int(obj["rep"]) for obj in data_list if data_list]
                context["data_rep"] = data_rep
                data_resp = [int(obj["resp"]) for obj in data_list if data_list]
                context["data_resp"] = data_resp
                data_submit = [int(obj["submit"]) for obj in data_list if data_list]
                context["data_submit"] = data_submit
                data_mt = [int(obj["mt"]) for obj in data_list if data_list]
                context["data_mt"] = data_mt
                data_no_submit = [int(obj["no_submit"]) for obj in data_list if data_list]
                context["no_submit"] = data_no_submit
                data_no_response = [int(obj["no_response"]) for obj in data_list if data_list]
                context["no_response"] = data_no_response
                context["data_y"] = max(max(data_rep), max(data_resp), max(data_submit), max(data_mt),
                                        max(data_no_submit), max(data_no_response))
                return json_response(data=context)
            # 按天显示
            if data_type == 2:
                # 查询数据
                sql = """SELECT 
                h.data_day AS data_day,
                SUM(h.mt) AS mt,
                SUM(h.submit) AS submit,
                SUM(h.resp) AS resp,
                SUM(h.report) AS rep,
                d.no_submit,
                d.no_response
                FROM sms_hour_data h
                LEFT JOIN 
                sms_day_data d ON h.data_day=d.data_day
                WHERE h.data_day>='%s' AND h.data_day<'%s'
                GROUP BY h.data_day""" % (begin_day, end_day)
                data_list = execute('mobile_sms', sql)
                data_list = tuple(data_list)
                context["data_x"] = [obj[0] for obj in data_list]
                data_rep = [int(obj[4]) for obj in data_list if data_list]
                context["data_rep"] = data_rep
                data_resp = [int(obj[3]) for obj in data_list if data_list]
                context["data_resp"] = data_resp
                data_submit = [int(obj[2]) for obj in data_list if data_list]
                context["data_submit"] = data_submit
                data_mt = [int(obj[1]) for obj in data_list if data_list]
                context["data_mt"] = data_mt
                data_no_submit = [int(obj[5]) if obj[5] else 0 for obj in data_list if data_list]
                context["no_submit"] = data_no_submit
                data_no_response = [int(obj[6]) if obj[6] else 0 for obj in data_list if data_list]
                context["no_response"] = data_no_response
                # 查询纵坐标最大值
                context["data_y"] = max(max(data_rep), max(data_resp), max(data_submit), max(data_mt))
                return json_response(data=context)
            # 按月显示
            if data_type == 3:
                # 查询数据
                sql = """SELECT 
                SUBSTR(h.data_day FROM 1 FOR 6) AS data_mon,
                SUM(h.mt) AS mt,
                SUM(h.submit) AS submit,
                SUM(h.resp) AS resp,
                SUM(h.report) AS rep,
                SUM(DISTINCT d.no_submit) AS no_submit,
                SUM(DISTINCT d.no_response) AS no_response
                FROM sms_hour_data h
                LEFT JOIN 
                sms_day_data d ON h.data_day=d.data_day
                WHERE h.data_day>='%s' AND h.data_day<'%s'
                GROUP BY SUBSTR(h.data_day FROM 1 FOR 6)""" % (begin_day, end_day)
                data_list = execute('mobile_sms', sql)
                # 数据处理
                data_list = tuple(data_list)
                context["data_x"] = [str(obj[0]) for obj in data_list if data_list]
                data_rep = [int(obj[4]) for obj in data_list if data_list]
                context["data_rep"] = data_rep
                data_resp = [int(obj[3]) for obj in data_list if data_list]
                context["data_resp"] = data_resp
                data_submit = [int(obj[2]) for obj in data_list if data_list]
                context["data_submit"] = data_submit
                data_mt = [int(obj[1]) for obj in data_list if data_list]
                context["data_mt"] = data_mt
                data_no_submit = [int(obj[5]) if obj[5] else 0 for obj in data_list if data_list]
                context["no_submit"] = data_no_submit
                data_no_response = [int(obj[6]) if obj[6] else 0 for obj in data_list if data_list]
                context["no_response"] = data_no_response
                # 查询纵坐标最大值
                context["data_y"] = max(max(data_rep), max(data_resp), max(data_submit), max(data_mt))
                return json_response(data=context)

        except Exception as e:
            traceback.print_exc()
            log.error("%s:%s" % (inspect.stack()[0][3], e))
            return json_response(code="error", msg="查询失败，请重新查询！")


class SmsDetailAPI(Resource):

    @staticmethod
    def post():
        """
        说明：查看短信详情
        可以查看每日、每月的短信详情
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        吕建威         2018-10-23
        ----------------------------------------
        """
        parser = reqparse.RequestParser()
        parser.add_argument("data_date", required=True, help="请选择时间")
        args = parser.parse_args()
        # 获取参数值
        data_date = str(args.data_date)
        context = {}
        try:
            if len(data_date) == 8:
                sql = """SELECT data_hour, report, resp, submit, mt FROM sms_hour_data WHERE data_day = '{data_date}'
                """.format(data_date=data_date)
                data_list = execute('mobile_sms', sql)
                # 处理查询结果
                data_list = tuple(data_list)
                data_x = [int(obj[0]) for obj in data_list if data_list]
                context["data_x"] = data_x
                data_rep = [int(obj[1]) for obj in data_list if data_list]
                context["data_rep"] = data_rep
                data_resp = [int(obj[2]) for obj in data_list if data_list]
                context["data_resp"] = data_resp
                data_submit = [int(obj[3]) for obj in data_list if data_list]
                context["data_submit"] = data_submit
                data_mt = [int(obj[4]) for obj in data_list if data_list]
                context["data_mt"] = data_mt
                context["data_y"] = max(max(data_rep), max(data_resp), max(data_submit), max(data_mt))
                return json_response(data=context)
            # 日维度数据
            if len(data_date) == 6:
                # 结束时间处理
                begin_date = str(data_date + "01")
                begin_day = int("%d%.2d%.2d" % (int(begin_date[:4]), int(begin_date[4:6]), 1))
                begin_date = datetime.date(int(begin_date[:4]), int(begin_date[4:6]), 1)
                end_date = r_next_month(begin_date)
                # 将开始时间和截止时间转换为数据库可接受的类型
                end_day = int("%d%.2d%.2d" % (end_date.year, end_date.month, end_date.day))
                sql = """SELECT 
                h.data_day AS data_day,
                SUM(h.mt) AS mt,
                SUM(h.submit) AS submit,
                SUM(h.resp) AS resp,
                SUM(h.report) AS rep,
                d.no_submit,
                d.no_response
                FROM sms_hour_data h
                LEFT JOIN 
                sms_day_data d ON h.data_day=d.data_day
                WHERE h.data_day>='%s' AND h.data_day<'%s'
                GROUP BY h.data_day""" % (begin_day, end_day)
                data_list = execute('mobile_sms', sql)
                # 结果处理 将数据库查询结果转化为 tuple
                data_list = tuple(data_list)
                context["data_x"] = [str(obj[0]) for obj in data_list if data_list]
                data_rep = [int(obj[4]) for obj in data_list if data_list]
                context["data_rep"] = data_rep
                data_resp = [int(obj[3]) for obj in data_list if data_list]
                context["data_resp"] = data_resp
                data_submit = [int(obj[2]) for obj in data_list if data_list]
                context["data_submit"] = data_submit
                data_mt = [int(obj[1]) for obj in data_list if data_list]
                context["data_mt"] = data_mt
                data_no_submit = [int(obj[5]) if obj[5] else 0 for obj in data_list if data_list]
                context["no_submit"] = data_no_submit
                data_no_response = [int(obj[6]) if obj[6] else 0 for obj in data_list if data_list]
                context["no_response"] = data_no_response
                # 查询纵坐标最大值
                context["data_y"] = max(max(data_rep), max(data_resp), max(data_submit), max(data_mt))
                return json_response(data=context)
        except Exception as e:
            traceback.print_exc()
            log.error("%s:%s" % (inspect.stack()[0][3], e))
        return json_response(code="error", msg="查询失败，请重新查询！")


class SmsFailAPI(Resource):
    @staticmethod
    def post():
        """
        说明：状态报告失败数据明细
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        吕建威         2018-10-23
        ----------------------------------------
        """
        parser = reqparse.RequestParser()
        parser.add_argument("data_type", required=True, help="请选择查询类型")
        parser.add_argument("data_date", required=True, help="请选择查询日期")
        args = parser.parse_args()
        # 获取参数值
        data_type = int(args.data_type)
        data_date = args.data_date
        context = {}
        try:
            # 以日为维度
            if data_type == 2:
                sql = """SELECT report_code, rep_num FROM sms_rep_detail WHERE data_day = '{data_date}'""".format(data_date=data_date)
                data_list = execute('mobile_sms', sql)
                data_list = list(data_list)
                mt_ok = 0
                for obj in data_list:
                    if obj["report_code"] == "DELIVRD":
                        mt_ok = int(obj[1])
                        data_list.remove(obj)
                context["data_date"] = data_date
                context["mt_ok"] = mt_ok
                data_x = [str(obj[0]) for obj in data_list if data_list]
                context["data_x"] = data_x
                rep_num = [int(obj[1]) for obj in data_list if data_list]
                context["rep_num"] = rep_num
                context["data_y"] = max(rep_num) if rep_num else 0
            # 以月为维度
            if data_type == 3:
                begin_date = str(data_date + "01")
                begin_day = int("%d%.2d%.2d" % (int(begin_date[:4]), int(begin_date[4:6]), 1))
                begin_date = datetime.date(int(begin_date[:4]), int(begin_date[4:6]), 1)
                end_date = r_next_month(begin_date)
                # 将开始时间和截止时间转换为数据库可接受的类型
                end_day = int("%d%.2d%.2d" % (end_date.year, end_date.month, end_date.day))
                sql = """SELECT 
                report_code,
                SUM(rep_num) AS rep_num
                FROM sms_rep_detail
                WHERE data_day>='%s' AND data_day<'%s'
                GROUP BY report_code""" % (begin_day, end_day)
                data_list = execute('mobile_sms', sql)
                data_list = list(data_list)
                mt_ok = 0
                # report_code 为 DELIVRD 代表发送成功
                for obj in data_list:
                    if obj[0] == "DELIVRD":
                        mt_ok = int(obj[1])
                        data_list.remove(obj)
                context["data_date"] = data_date
                data_x = [str(obj[0]) for obj in data_list if data_list]
                context["data_x"] = data_x
                rep_num = [int(obj[1]) for obj in data_list if data_list]
                context["rep_num"] = rep_num if rep_num else 0
                context["data_y"] = max(rep_num)
                context["mt_ok"] = mt_ok
            print(type(context))
            return json_response(data=context)
        except Exception as e:
            traceback.print_exc()
            log.error("%s:%s" % (inspect.stack()[0][3], e))
        return json_response(code="error", msg="查询失败，请重新查询！")
