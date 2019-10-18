# coding=utf-8
# @Time    : 2018-12-19 16:12
# @Author  : 张嘉麒
# @File    : expand.py
import datetime

from flask_restful import Resource, reqparse

from application import db
from apps.statist.common.task_common import day_range, month_range, stu_expand_data_handle
from apps.utils.res import json_response


class ExpandApi(Resource):

    @staticmethod
    def get():
        """
        说明：课外拓展数据统计默认接口
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        张嘉麒         2018-12-19
        ----------------------------------------
        """
        end_time_date = datetime.datetime.now()
        end_time_stamp = int(end_time_date.timestamp())
        begin_time_stamp = end_time_stamp - 60 * 60 * 24 * 6
        begin_time = datetime.datetime.fromtimestamp(begin_time_stamp).strftime("%Y%m%d")
        end_time = datetime.datetime.fromtimestamp(end_time_stamp).strftime("%Y%m%d")
        # 时间轴
        x_asix = [str(datetime.datetime.fromtimestamp(end_time_stamp - 3600 * 24 * (i - 1)).strftime("%Y%m%d")) for i in
                  range(7, 0, -1)]

        data_sql = """
                            SELECT
                                data_day, 
                                sx_susuanleyuan,
                                sx_aoshutiantianlian,
                                sx_xiaoxuejiaocaijiangjie,
                                sx_chuzhongjiaocaijiangjie,
                                sx_xiaoxuelianxicejiangjie,
                                yw_xuexiezi,
                                yw_shengcitingxie,
                                yw_yuedulijie,
                                yw_chengyuyouxi,
                                yw_shicidazhan,
                                yy_kebendianduji,
                                yy_baopoqiqiu,
                                yy_dadishu
                            FROM
                                tbkt_statistics.statist_stu_expand
                            WHERE 
                                data_day BETWEEN %s and %s
                            GROUP BY 
                                data_day
                            ORDER BY
                                data_day
                           """ % (begin_time, end_time)
        data = db.get_engine(bind='statist').execute(data_sql)
        d = stu_expand_data_handle(data, x_asix)
        return json_response(data=d)

    @staticmethod
    def post():
        """
        说明：课外拓展数据统计默认接口
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        张嘉麒         2018-12-19
        ----------------------------------------
        """
        parser = reqparse.RequestParser()
        parser.add_argument("begin_time")
        parser.add_argument("end_time")
        parser.add_argument("q_type", required=True, help="没有查询类型")
        args = parser.parse_args()
        # 获取参数值
        begin_time = args.begin_time
        end_time = args.end_time
        q_type = args.q_type
        if not end_time:
            end_time_date = datetime.datetime.now()
            end_time_stamp = int(end_time_date.timestamp())
            begin_time_stamp = end_time_stamp - 60 * 60 * 24 * 6
            begin_time = datetime.datetime.fromtimestamp(begin_time_stamp).strftime("%Y%m%d")
            end_time = datetime.datetime.fromtimestamp(end_time_stamp).strftime("%Y%m%d")
        else:
            end_time_stamp = end_time
            begin_time_stamp = begin_time
            # 开始时间和结束时间到天
            begin_time = datetime.datetime.fromtimestamp(int(begin_time_stamp)).strftime("%Y%m%d")
            end_time = datetime.datetime.fromtimestamp(int(end_time_stamp)).strftime("%Y%m%d")

        # q_type 查询方式 1 按天 2 按月
        if q_type == "1":
            x_asix = day_range(begin_time, end_time)
            # 数据按时间和学科分组
            post_data_sql = """
                            SELECT
                                data_day, 
                                SUM(sx_susuanleyuan) as sx_susuanleyuan,
                                SUM(sx_aoshutiantianlian) as sx_aoshutiantianlian,
                                SUM(sx_xiaoxuejiaocaijiangjie) as sx_xiaoxuejiaocaijiangjie,
                                SUM(sx_chuzhongjiaocaijiangjie) as sx_chuzhongjiaocaijiangjie,
                                SUM(sx_xiaoxuelianxicejiangjie) as sx_xiaoxuelianxicejiangjie,
                                SUM(yw_xuexiezi) as yw_xuexiezi,
                                SUM(yw_shengcitingxie) as yw_shengcitingxie,
                                SUM(yw_yuedulijie) as yw_yuedulijie,
                                SUM(yw_chengyuyouxi) as yw_chengyuyouxi,
                                SUM(yw_shicidazhan) as yw_shicidazhan,
                                SUM(yy_kebendianduji) as yy_kebendianduji,
                                SUM(yy_baopoqiqiu) as yy_baopoqiqiu,
                                SUM(yy_dadishu) as yy_dadishu
                            FROM
                                tbkt_statistics.statist_stu_expand
                            WHERE 
                                data_day BETWEEN %s and %s
                            GROUP BY 
                                data_day
                            ORDER BY
                                data_day
                            """ % (begin_time, end_time)
        # q_type == "2" 时候
        else:
            x_asix = month_range(begin_time, end_time)
            post_data_sql = """
                            SELECT
                                LEFT (data_day, 6) as data_month, 
                                SUM(sx_susuanleyuan) as sx_susuanleyuan,
                                SUM(sx_aoshutiantianlian) as sx_aoshutiantianlian,
                                SUM(sx_xiaoxuejiaocaijiangjie) as sx_xiaoxuejiaocaijiangjie,
                                SUM(sx_chuzhongjiaocaijiangjie) as sx_chuzhongjiaocaijiangjie,
                                SUM(sx_xiaoxuelianxicejiangjie) as sx_xiaoxuelianxicejiangjie,
                                SUM(yw_xuexiezi) as yw_xuexiezi,
                                SUM(yw_shengcitingxie) as yw_shengcitingxie,
                                SUM(yw_yuedulijie) as yw_yuedulijie,
                                SUM(yw_chengyuyouxi) as yw_chengyuyouxi,
                                SUM(yw_shicidazhan) as yw_shicidazhan,
                                SUM(yy_kebendianduji) as yy_kebendianduji,
                                SUM(yy_baopoqiqiu) as yy_baopoqiqiu,
                                SUM(yy_dadishu) as yy_dadishu
                            FROM
                                tbkt_statistics.statist_stu_expand
                            WHERE 
                                data_day BETWEEN %s and %s
                            GROUP BY 
                                data_month
                            ORDER BY
                                data_month
                            """ % (begin_time, end_time)
        data = db.get_engine(bind='statist').execute(post_data_sql)
        d = stu_expand_data_handle(data, x_asix)

        return json_response(data=d)
