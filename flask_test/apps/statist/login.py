import traceback
import inspect
import logging
import datetime
from application import db
from apps.utils.res import json_response
from flask_restful import Resource, reqparse
from libs.common import date_to_unix, from_unixtime
log = logging.getLogger(__name__)


class LoginAPI(Resource):

    @staticmethod
    def post():
        """
        说明：登录统计
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        吕建威         2018-10-23
        ----------------------------------------
        """
        parser = reqparse.RequestParser()
        parser.add_argument("login_type", required=True, help="请选择查询类型")
        parser.add_argument("begin_date")
        parser.add_argument("end_date")
        args = parser.parse_args()
        # 获取参数值
        login_type = int(args.login_type) if args.login_type else 1
        begin_date = int(args.begin_date) if args.begin_date else ""
        end_date = int(args.end_date) if args.end_date else ""
        context = {}
        try:
            if begin_date == '' and end_date == '':
                end_date = datetime.datetime.now()
                begin_date = end_date - datetime.timedelta(days=7)
            elif begin_date == '':
                end_date = from_unixtime(end_date)
                begin_date = end_date - datetime.timedelta(days=7)
            elif end_date == '':
                begin_date = from_unixtime(begin_date)
                end_date = datetime.datetime.now() + datetime.timedelta(days=1)
            else:
                begin_date = from_unixtime(begin_date)
                end_date = from_unixtime(end_date)
                end_date = end_date + datetime.timedelta(days=1)
            begin_date = begin_date.strftime("%Y%m%d")
            end_date = end_date.strftime("%Y%m%d")
            if login_type == 1:
                login_list = "('1')"
            elif login_type == 2:
                login_list = "('2')"
            elif login_type == 3:
                login_list = "('3')"
            else:
                login_list = "('1', '2', '3')"
            sql = """
            SELECT
                data_day,
                SUM(stu_num),
                SUM(tea_num),
                SUM(stu_time),
                SUM(tea_time),
                SUM(stu_open_num),
                SUM(tea_open_num)
            FROM
                tbkt_statistics.statist_login 
            WHERE
                platform IN {login_list} 
                AND data_day >= '{begin_date}' 
                AND data_day <= '{end_date}' 
            GROUP BY data_day;
            """.format(login_list=login_list, begin_date=begin_date, end_date=end_date)
            data_list = db.get_engine(bind='statist').execute(sql)
            data_list = tuple(data_list)
            data_day = [int(i[0]) for i in data_list]
            stu_num = [int(i[1]) for i in data_list]
            tea_num = [int(i[2]) for i in data_list]
            stu_time = [int(i[3]) for i in data_list]
            tea_time = [int(i[4]) for i in data_list]
            stu_open_num = [int(i[5]) for i in data_list]
            tea_open_num = [int(i[6]) for i in data_list]
            context["data_day"] = data_day
            context["stu_num"] = stu_num
            context["tea_num"] = tea_num
            context["stu_time"] = stu_time
            context["tea_time"] = tea_time
            context["stu_open_num"] = stu_open_num
            context["tea_open_num"] = tea_open_num
            context['data_y'] = max(max(stu_num), max(tea_num), max(stu_time),
                                    max(tea_time), max(stu_open_num), max(tea_open_num))
            return json_response(data=context)
        except Exception as e:
            traceback.print_exc()
            log.error("%s:%s" % (inspect.stack()[0][3], e))
            return json_response(code="error", msg="查询失败，请重新查询！")