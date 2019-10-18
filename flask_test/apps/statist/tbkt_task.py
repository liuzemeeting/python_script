# @File  : tbkt_task.py
# @Author: 王世成
# @Date  : 2019/7/29
# @Desc  :
import datetime
import time
from collections import defaultdict

from flask_restful import Resource, reqparse

from application import db
from apps.statist.common.task_common import Struct
from apps.utils.res import json_response


class TaskCommon(Resource):
    @staticmethod
    def fetchall(sql):
        # tuple to Struct(dict)
        return [Struct(dict(zip(i.keys(), i))) for i in db.get_engine(bind="devops").execute(sql).fetchall()]

    @staticmethod
    def make_date_series(begin_date, end_date):
        # 生成连续时间
        days = [begin_date]
        dt = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        date = begin_date
        while date <= end_date:
            dt += datetime.timedelta(days=1)
            date = dt.strftime("%Y-%m-%d")
            days.append(date)
        return days


class TbktTaskAPI(TaskCommon):
    def get_accept(self, user_ids, start_date, end_date):
        print(",".join(user_ids))
        # 获取接收任务数
        sql = """
        SELECT
            FROM_UNIXTIME(due_date, '%%%%Y-%%%%m-%%%%d') date,
            count(1) num,
            user_id
        FROM
            agile_issues 
        WHERE
            user_id in ({user_ids})
            and tracker_id = 1
            and due_date between {start_date} and {end_date}  
        GROUP BY
            FROM_UNIXTIME( due_date, '%%%%Y-%%%%m-%%%%d' ), user_id;
        """.format(user_ids=user_ids, start_date=start_date, end_date=end_date)
        data = self.fetchall(sql)
        return data

    def task_count(self, user_ids, start_date, end_date):
        # 获取发布任务数
        cond = f" and (user_id in ({','.join(user_ids)}) or assigned_to_id in ({','.join(user_ids)}))" if user_ids else ""
        sql = """
        SELECT   
            i.created_on,
            i.user_id,
            (select nickname from account_users where id = i.user_id) create_nickname,
            assigned_to_id,
            (select nickname from account_users where id = i.assigned_to_id) assigned_nickname,
            FROM_UNIXTIME( i.due_date, '%%Y-%%m-%%d') < FROM_UNIXTIME( s.created_on, '%%Y-%%m-%%d') is_delay
        FROM
            agile_issues i left join
            agile_journals s on i.id = s.issues_id 
            inner join 
            agile_journal_details d on  s.id = d.journal_id and d.prop_key = 'status_id' and value = 3
        where 
            i.tracker_id not in (2, 5, 8)
            {cond}
            and i.created_on between {start_date} and {end_date}; 
        """.format(cond=cond, start_date=start_date, end_date=end_date)
        return self.fetchall(sql)

    def get_user(self, user_ids):
        # 获取用户信息
        sql = """
        select id, nickname from account_users where id in (%s)
        """ % ",".join(user_ids)
        return self.fetchall(sql)

    @staticmethod
    def get_default_date():
        mk = lambda x: int(time.mktime(x.timetuple()))
        end_date = datetime.date.today() + datetime.timedelta(days=1)
        start_date = end_date.replace(day=1)
        return mk(start_date), mk(end_date)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("start_date")
        parser.add_argument("end_date")
        parser.add_argument("follow_user")
        args = parser.parse_args()
        start_date, end_date, follow_user = args.start_date, args.end_date, args.follow_user
        follow_user = follow_user.split(",") if follow_user else None
        if not start_date:
            start_date, end_date = self.get_default_date()
        task_list = self.task_count(follow_user, start_date, end_date)
        push_map = defaultdict(int)
        assigned_map = defaultdict(int)
        delay_map = defaultdict(int)
        for i in task_list:
            push_map[(i.user_id, i.create_nickname)] += 1
            assigned_map[(i.assigned_to_id, i.assigned_nickname)] += 1
            if i.is_delay:
                delay_map[(i.assigned_to_id, i.assigned_nickname)] += 1
        temp = set(list(push_map.keys()) + list(assigned_map.keys()) + list(delay_map.keys()))
        out = []
        for user_id, name in sorted(temp, key=lambda x: x[0]):
            if follow_user and str(user_id) not in follow_user:
                continue
            k = (user_id, name)
            d = dict(
                user_id=user_id,
                name=name,
                push=push_map.get(k, 0),
                assigned=assigned_map.get(k, 0),
                delay=delay_map.get(k, 0)
            )
            out.append(d)
        return json_response(data=out)
