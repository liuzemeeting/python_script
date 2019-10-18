import datetime

from flask_restful import Resource, reqparse

from application import db
from apps.statist.common.task_common import Struct
from apps.utils.res import json_response


class MoneyDataAPI(Resource):

    @staticmethod
    def get():
        """
        说明：计费金额统计
        ----------------------------------------
        修改人          修改日期          修改原因
        ----------------------------------------
        张栋梁         2018-10-22
        ----------------------------------------
        """
        end_time_date = datetime.datetime.now()
        end_time_stamp = int(end_time_date.timestamp())
        begin_time_stamp = end_time_stamp - 60 * 60 * 24 * 6
        # # 时间轴
        # x_asix = [str(datetime.datetime.fromtimestamp(end_time_stamp - 3600 * 24 * (i - 1)).strftime("%Y-%m-%d")) for i in
        #           range(7, 0, -1)]
        data_sql = """
                  SELECT
                        coin_date,
                        all_num,
                        all_coin,
                        a_num,
                        a_coin,
                        b_num,
                        b_coin,
                        c_num,
                        c_coin,
                        d_num,
                        d_coin,
                        e_num,
                        e_coin
                    FROM
                        tbkt_statistics.expenses_data 
                    WHERE
                        UNIX_TIMESTAMP( coin_date ) BETWEEN %s 
                        AND %s
                    ORDER BY coin_date
                   """ % (begin_time_stamp, end_time_stamp)
        data = db.get_engine(bind='statist').execute(data_sql)
        context = Struct()
        res = Struct()
        x_axis = []
        all_num_list = []
        all_coin_list = []
        a_num_list = []
        a_coin_list = []
        b_num_list = []
        b_coin_list = []
        c_num_list = []
        c_coin_list = []
        d_num_list = []
        d_coin_list = []
        e_num_list = []
        e_coin_list = []
        for d in data:
            x_axis.append(d[0])
            all_num_list.append(str(d[1]))
            all_coin_list.append(str(d[2]))
            a_num_list.append(str(d[3]))
            a_coin_list.append(str(d[4]))
            b_num_list.append(str(d[5]))
            b_coin_list.append(str(d[6]))
            c_num_list.append(str(d[7]))
            c_coin_list.append(str(d[8]))
            d_num_list.append(str(d[9]))
            d_coin_list.append(str(d[10]))
            e_num_list.append(str(d[11]))
            e_coin_list.append(str(d[12]))
        res.x_axis = x_axis
        context.all_num_list = all_num_list
        context.all_coin_list = all_coin_list
        context.a_num_list = a_num_list
        context.a_coin_list = a_coin_list
        context.b_num_list = b_num_list
        context.b_coin_list = b_coin_list
        context.c_num_list = c_num_list
        context.c_coin_list = c_coin_list
        context.d_num_list = d_num_list
        context.d_coin_list = d_coin_list
        context.e_num_list = e_num_list
        context.e_coin_list = e_coin_list
        res.context = context
        return json_response(data=res)

    @staticmethod
    def post():
        """
        说明：学生做作业数据统计查询接口
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
            # begin_time = datetime.datetime.fromtimestamp(begin_time_stamp).strftime("%Y%m%d")
            # end_time = datetime.datetime.fromtimestamp(end_time_stamp).strftime("%Y%m%d")
        else:
            end_time_stamp = end_time
            begin_time_stamp = begin_time
            # 开始时间和结束时间到天
            # begin_time = datetime.datetime.fromtimestamp(int(begin_time_stamp)).strftime("%Y%m%d")
            # end_time = datetime.datetime.fromtimestamp(int(end_time_stamp)).strftime("%Y%m%d")

        # q_type 查询方式 1 按天 2 按月
        if q_type == "1":
            # 数据按时间和学科分组
            post_data_sql = """
                            SELECT
                                coin_date,
                                all_num,
                                all_coin,
                                a_num,
                                a_coin,
                                b_num,
                                b_coin,
                                c_num,
                                c_coin,
                                d_num,
                                d_coin,
                                e_num,
                                e_coin
                            FROM
                                tbkt_statistics.expenses_data 
                            WHERE
                                UNIX_TIMESTAMP( coin_date ) BETWEEN %s 
                                AND %s
                            ORDER BY coin_date
                            """ % (begin_time_stamp, end_time_stamp)
        if q_type == "2":
            post_data_sql = """
                            SELECT
                                SUBSTR(coin_date,1,7) as date,
                                sum(all_num),
                                sum(all_coin),
                                sum(a_num),
                                sum(a_coin),
                                sum(b_num),
                                sum(b_coin),
                                sum(c_num),
                                sum(c_coin),
                                sum(d_num),
                                sum(d_coin),
                                sum(e_num),
                                sum(e_coin)
                            FROM
                                tbkt_statistics.expenses_data 
                            WHERE
                                UNIX_TIMESTAMP( coin_date ) BETWEEN %s
                                AND %s 
                            GROUP BY
                                SUBSTR(coin_date,1,7)
                            ORDER BY SUBSTR(coin_date,1,7)
                            """ % (begin_time, end_time)
        data = db.get_engine(bind='statist').execute(post_data_sql)
        context = Struct()
        res = Struct()
        x_axis = []
        all_num_list = []
        all_coin_list = []
        a_num_list = []
        a_coin_list = []
        b_num_list = []
        b_coin_list = []
        c_num_list = []
        c_coin_list = []
        d_num_list = []
        d_coin_list = []
        e_num_list = []
        e_coin_list = []
        for d in data:
            x_axis.append(d[0])
            all_num_list.append(str(d[1]))
            all_coin_list.append(str(d[2]))
            a_num_list.append(str(d[3]))
            a_coin_list.append(str(d[4]))
            b_num_list.append(str(d[5]))
            b_coin_list.append(str(d[6]))
            c_num_list.append(str(d[7]))
            c_coin_list.append(str(d[8]))
            d_num_list.append(str(d[9]))
            d_coin_list.append(str(d[10]))
            e_num_list.append(str(d[11]))
            e_coin_list.append(str(d[12]))
        context.all_num_list = all_num_list
        context.all_coin_list = all_coin_list
        context.a_num_list = a_num_list
        context.a_coin_list = a_coin_list
        context.b_num_list = b_num_list
        context.b_coin_list = b_coin_list
        context.c_num_list = c_num_list
        context.c_coin_list = c_coin_list
        context.d_num_list = d_num_list
        context.d_coin_list = d_coin_list
        context.e_num_list = e_num_list
        context.e_coin_list = e_coin_list
        res.context = context
        res.x_axis = x_axis
        return json_response(data=res)
