# coding=utf-8
# @Time    : 2018/10/22 下午3:24
# @Author  : Zuyong Du
import datetime

from flask_restful import Resource, reqparse

from application import db
from apps.statist.common.task_common import tea_task_data_handle, day_range, month_range
from apps.utils.res import json_response


class TaskTeaAPI(Resource):

    @staticmethod
    def get():
        """
        说明：教师发作业统计默认数据
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        张栋梁          2018-10-22
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
                          sid,
                          data_day, 
                          SUM(tongbuxiti) as tongbuxiti,
                          SUM(danyuanfuxi) as danyuanfuxi,
                          SUM(gaopincuoti) as gaopincuoti,
                          SUM(shengcitingxie) as shengcitingxie,
                          SUM(biaoziranduan) as biaoziranduan,
                          SUM(kewenlangdu) as kewenlangdu,
                          SUM(xuexiezi) as xuexiezi,
                          SUM(kewaiyuedu) as kewaiyuedu,
                          SUM(danxigendu) as danxigendu,
                          SUM(kewengendu) as kewengendu,
                          SUM(susuan) as susuan,
                          SUM(zhishidianshipin) as zhishidianshipin,
                          SUM(kewaituozhan) as kewaituozhan,
                          SUM(jiaxiaogoutong) as jiaxiaogoutong
                      FROM
                          tbkt_statistics.statist_tea_task
                      WHERE 
                          data_day BETWEEN %s and %s
                      GROUP BY 
                          data_day,
                          sid
                      ORDER BY
                          data_day
                   """ % (begin_time, end_time)

        data = db.get_engine(bind='statist').execute(data_sql)

        d = tea_task_data_handle(data, x_asix)
        return json_response(data=d)

    @staticmethod
    def post():
        """
        说明：教师发作业统计查询接口
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        张栋梁          2018-10-22
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
                            sid,
                            data_day, 
                            SUM(tongbuxiti) as tongbuxiti,
                            SUM(danyuanfuxi) as danyuanfuxi,
                            SUM(gaopincuoti) as gaopincuoti,
                            SUM(shengcitingxie) as shengcitingxie,
                            SUM(biaoziranduan) as biaoziranduan,
                            SUM(kewenlangdu) as kewenlangdu,
                            SUM(xuexiezi) as xuexiezi,
                            SUM(kewaiyuedu) as kewaiyuedu,
                            SUM(danxigendu) as danxigendu,
                            SUM(kewengendu) as kewengendu,
                            SUM(susuan) as susuan,
                            SUM(zhishidianshipin) as zhishidianshipin,
                            SUM(kewaituozhan) as kewaituozhan,
                            SUM(jiaxiaogoutong) as jiaxiaogoutong
                        FROM
                            tbkt_statistics.statist_tea_task
                        WHERE 
                            data_day BETWEEN %s and %s
                        GROUP BY 
                            data_day,
                            sid
                        ORDER BY
                            data_day
                       """ % (begin_time, end_time)
        if q_type == "2":
            x_asix = month_range(begin_time, end_time)
            post_data_sql = """
                        SELECT
                            sid,
                            LEFT (data_day, 6) as data_month, 
                            SUM(tongbuxiti) as tongbuxiti,
                            SUM(danyuanfuxi) as danyuanfuxi,
                            SUM(gaopincuoti) as gaopincuoti,
                            SUM(shengcitingxie) as shengcitingxie,
                            SUM(biaoziranduan) as biaoziranduan,
                            SUM(kewenlangdu) as kewenlangdu,
                            SUM(xuexiezi) as xuexiezi,
                            SUM(kewaiyuedu) as kewaiyuedu,
                            SUM(danxigendu) as danxigendu,
                            SUM(kewengendu) as kewengendu,
                            SUM(susuan) as susuan,
                            SUM(zhishidianshipin) as zhishidianshipin,
                            SUM(kewaituozhan) as kewaituozhan,
                            SUM(jiaxiaogoutong) as jiaxiaogoutong
                        FROM
                            tbkt_statistics.statist_tea_task
                        WHERE 
                            data_day BETWEEN %s and %s
                        GROUP BY 
                            data_month,
                            sid
                        ORDER BY
                            data_month
                       """ % (begin_time, end_time)
        data = db.get_engine(bind='statist').execute(post_data_sql)
        d = tea_task_data_handle(data, x_asix)
        
        return json_response(data=d)
