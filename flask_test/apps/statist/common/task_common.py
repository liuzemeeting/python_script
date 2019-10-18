import datetime


class Struct(dict):
    """
    为字典加上点语法. 例如:
    >>> o = Struct({'a':1})
    >>> o.a
    >>> 1
    >>> o.b
    >>> None
    """

    def __init__(self, *e, **f):
        if e:
            self.update(e[0])
        if f:
            self.update(f)

    def __getattr__(self, name):
        # Pickle is trying to get state from your object, and dict doesn't implement it.
        # Your __getattr__ is being called with "__getstate__" to find that magic method,
        # and returning None instead of raising AttributeError as it should.
        if name.startswith('__'):
            raise AttributeError
        return self.get(name)

    def __setattr__(self, name, val):
        self[name] = val

    def __delattr__(self, name):
        self.pop(name, None)

    def __hash__(self):
        return id(self)


def tea_task_data_handle(data, x_asix):
    """
    说明：教师发作业数据处理
    ----------------------------------------
    修改人          修改日期          修改原因
    ----------------------------------------
    张栋梁          2018-10-22
    ----------------------------------------
    """
    d = Struct()
    context = Struct()
    context.sx_tongbuxiti = []
    context.sx_danyuanfuxi = []
    context.sx_gaopincuoti = []
    context.sx_susuan = []
    context.sx_zhishidianshipin = []
    context.sx_kewaituozhan = []
    context.sx_jiaxiaogoutong = []
    context.sx2_tongbuxiti = []
    context.sx2_danyuanfuxi = []
    context.sx2_gaopincuoti = []
    context.sx2_kewaituozhan = []
    context.sx2_jiaxiaogoutong = []
    context.yw_tongbuxiti = []
    context.yw_danyuanfuxi = []
    context.yw_gaopincuoti = []
    context.yw_shengcitingxie = []
    context.yw_biaoziranduan = []
    context.yw_kewenlangdu = []
    context.yw_xuexiezi = []
    context.yw_kewaiyuedu = []
    context.yw_kewaituozhan = []
    context.yw_jiaxiaogoutong = []
    context.yy_tongbuxiti = []
    context.yy_danyuanfuxi = []
    context.yy_gaopincuoti = []
    context.yy_dancigendu = []
    context.yy_kewengendu = []
    context.yy_kewaituozhan = []
    context.yy_jiaxiaogoutong = []
    context.yy2_tongbuxiti = []
    context.yy2_danyuanfuxi = []
    context.yy2_gaopincuoti = []
    context.yy2_kewaituozhan = []
    context.yy2_jiaxiaogoutong = []
    # 拼装数据
    for message in data:
        sid = message[0]
        day_data = message[1]
        if sid == 21:
            context.sx_tongbuxiti.append([day_data, message[2]])
            context.sx_danyuanfuxi.append([day_data, message[3]])
            context.sx_gaopincuoti.append([day_data, message[4]])
            context.sx_susuan.append([day_data, message[12]])
            context.sx_zhishidianshipin.append([day_data, message[13]])
            context.sx_kewaituozhan.append([day_data, message[14]])
            context.sx_jiaxiaogoutong.append([day_data, message[15]])
        if sid == 22:
            context.sx2_tongbuxiti.append([day_data, message[2]])
            context.sx2_danyuanfuxi.append([day_data, message[3]])
            context.sx2_gaopincuoti.append([day_data, message[4]])
            context.sx2_kewaituozhan.append([day_data, message[14]])
            context.sx2_jiaxiaogoutong.append([day_data, message[15]])
        if sid == 51:
            context.yw_tongbuxiti.append([day_data, message[2]])
            context.yw_danyuanfuxi.append([day_data, message[3]])
            context.yw_gaopincuoti.append([day_data, message[4]])
            context.yw_shengcitingxie.append([day_data, message[5]])
            context.yw_biaoziranduan.append([day_data, message[6]])
            context.yw_kewenlangdu.append([day_data, message[7]])
            context.yw_xuexiezi.append([day_data, message[8]])
            context.yw_kewaiyuedu.append([day_data, message[9]])
            context.yw_kewaituozhan.append([day_data, message[14]])
            context.yw_jiaxiaogoutong.append([day_data, message[15]])
        if sid == 91:
            context.yy_tongbuxiti.append([day_data, message[2]])
            context.yy_danyuanfuxi.append([day_data, message[3]])
            context.yy_gaopincuoti.append([day_data, message[4]])
            context.yy_dancigendu.append([day_data, message[10]])
            context.yy_kewengendu.append([day_data, message[11]])
            context.yy_kewaituozhan.append([day_data, message[14]])
            context.yy_jiaxiaogoutong.append([day_data, message[15]])
        if sid == 92:
            context.yy2_tongbuxiti.append([day_data, message[2]])
            context.yy2_danyuanfuxi.append([day_data, message[3]])
            context.yy2_gaopincuoti.append([day_data, message[4]])
            context.yy2_kewaituozhan.append([day_data, message[14]])
            context.yy2_jiaxiaogoutong.append([day_data, message[15]])

    # 查看是否有某天没有数据
    for key, value in context.items():
        date_list = []
        for t in value:
            date_list.append(str(t[0]))
        for i, e in enumerate(x_asix):
            if e not in date_list:
                value.insert(i, [e, 0])
        for i, j in enumerate(value):
            value[i] = int(j[1])
    d.context = context
    d.x_asix = x_asix

    return d


def stu_task_data_handle(data, x_asix):
    """
    说明：学生做作业数据处理
    ----------------------------------------
    修改人          修改日期          修改原因
    ----------------------------------------
    张栋梁          2018-10-22
    ----------------------------------------
    """
    d = Struct()
    context = Struct()
    context.sx_tongbuxiti = []
    context.sx_danyuanfuxi = []
    context.sx_gaopincuoti = []
    context.sx_susuan = []
    context.sx_zhishidianshipin = []
    context.sx_kewaituozhan = []
    context.sx_jiaxiaogoutong = []
    context.sx_tongbuchuangguan = []
    context.sx2_tongbuxiti = []
    context.sx2_danyuanfuxi = []
    context.sx2_gaopincuoti = []
    context.sx2_kewaituozhan = []
    context.sx2_jiaxiaogoutong = []
    context.sx2_tongbuchuangguan = []
    context.yw_tongbuxiti = []
    context.yw_danyuanfuxi = []
    context.yw_gaopincuoti = []
    context.yw_shengcitingxie = []
    context.yw_biaoziranduan = []
    context.yw_kewenlangdu = []
    context.yw_xuexiezi = []
    context.yw_kewaiyuedu = []
    context.yw_kewaituozhan = []
    context.yw_jiaxiaogoutong = []
    context.yw_tongbuchuangguan = []
    context.yy_tongbuxiti = []
    context.yy_danyuanfuxi = []
    context.yy_gaopincuoti = []
    context.yy_dancigendu = []
    context.yy_kewengendu = []
    context.yy_kewaituozhan = []
    context.yy_jiaxiaogoutong = []
    context.yy_tongbuchuangguan = []
    context.yy2_tongbuxiti = []
    context.yy2_danyuanfuxi = []
    context.yy2_gaopincuoti = []
    context.yy2_kewaituozhan = []
    context.yy2_jiaxiaogoutong = []
    context.yy2_tongbuchuangguan = []
    # 拼装数据
    for message in data:
        sid = message[0]
        day_data = message[1]
        if sid == 21:
            context.sx_tongbuxiti.append((day_data, message[2]))
            context.sx_danyuanfuxi.append((day_data, message[3]))
            context.sx_gaopincuoti.append((day_data, message[4]))
            context.sx_susuan.append((day_data, message[12]))
            context.sx_zhishidianshipin.append((day_data, message[13]))
            context.sx_kewaituozhan.append((day_data, message[14]))
            context.sx_jiaxiaogoutong.append((day_data, message[15]))
            context.sx_tongbuchuangguan.append((day_data, message[16]))
        if sid == 22:
            context.sx2_tongbuxiti.append((day_data, message[2]))
            context.sx2_danyuanfuxi.append((day_data, message[3]))
            context.sx2_gaopincuoti.append((day_data, message[4]))
            context.sx2_kewaituozhan.append((day_data, message[14]))
            context.sx2_jiaxiaogoutong.append((day_data, message[15]))
            context.sx2_tongbuchuangguan.append((day_data, message[16]))
        if sid == 51:
            context.yw_tongbuxiti.append((day_data, message[2]))
            context.yw_danyuanfuxi.append((day_data, message[3]))
            context.yw_gaopincuoti.append((day_data, message[4]))
            context.yw_shengcitingxie.append((day_data, message[5]))
            context.yw_biaoziranduan.append((day_data, message[6]))
            context.yw_kewenlangdu.append((day_data, message[7]))
            context.yw_xuexiezi.append((day_data, message[8]))
            context.yw_kewaiyuedu.append((day_data, message[9]))
            context.yw_kewaituozhan.append((day_data, message[14]))
            context.yw_jiaxiaogoutong.append((day_data, message[15]))
            context.yw_tongbuchuangguan.append((day_data, message[16]))
        if sid == 91:
            context.yy_tongbuxiti.append((day_data, message[2]))
            context.yy_danyuanfuxi.append((day_data, message[3]))
            context.yy_gaopincuoti.append((day_data, message[4]))
            context.yy_dancigendu.append((day_data, message[10]))
            context.yy_kewengendu.append((day_data, message[11]))
            context.yy_kewaituozhan.append((day_data, message[14]))
            context.yy_jiaxiaogoutong.append((day_data, message[15]))
            context.yy_tongbuchuangguan.append((day_data, message[16]))
        if sid == 92:
            context.yy2_tongbuxiti.append((day_data, message[2]))
            context.yy2_danyuanfuxi.append((day_data, message[3]))
            context.yy2_gaopincuoti.append((day_data, message[4]))
            context.yy2_kewaituozhan.append((day_data, message[14]))
            context.yy2_jiaxiaogoutong.append((day_data, message[15]))
            context.yy2_tongbuchuangguan.append((day_data, message[16]))

    # 查看是否有某天没有数据
    for key, value in context.items():
        date_list = []
        for t in value:
            date_list.append(str(t[0]))
        for i, e in enumerate(x_asix):
            if e not in date_list:
                value.insert(i, [e, 0])
        for i, j in enumerate(value):
            value[i] = int(j[1])
    d.context = context
    d.x_asix = x_asix

    return d


def stu_expand_data_handle(data, x_asix):
    """
    说明：学生做作业数据处理
    ----------------------------------------
    修改人          修改日期          修改原因
    ----------------------------------------
    张嘉麒          2018-12-22
    ----------------------------------------
    """
    d = Struct()
    context = Struct()
    context.sx_susuanleyuan = []
    context.sx_aoshutiantianlian = []
    context.sx_xiaoxuejiaocaijiangjie = []
    context.sx_chuzhongjiaocaijiangjie = []
    context.sx_xiaoxuelianxicejiangjie = []
    context.yw_xuexiezi = []
    context.yw_shengcitingxie = []
    context.yw_yuedulijie = []
    context.yw_chengyuyouxi = []
    context.yw_shicidazhan = []
    context.yy_kebendianduji = []
    context.yy_baopoqiqiu = []
    context.yy_dadishu = []
    # 拼装数据
    for message in data:
        day_data = message[0]
        context.sx_susuanleyuan.append((day_data, message[1]))
        context.sx_aoshutiantianlian.append((day_data, message[2]))
        context.sx_xiaoxuejiaocaijiangjie.append((day_data, message[3]))
        context.sx_chuzhongjiaocaijiangjie.append((day_data, message[4]))
        context.sx_xiaoxuelianxicejiangjie.append((day_data, message[5]))
        context.yw_xuexiezi.append((day_data, message[6]))
        context.yw_shengcitingxie.append((day_data, message[7]))
        context.yw_yuedulijie.append((day_data, message[8]))
        context.yw_chengyuyouxi.append((day_data, message[9]))
        context.yw_shicidazhan.append((day_data, message[10]))
        context.yy_kebendianduji.append((day_data, message[11]))
        context.yy_baopoqiqiu.append((day_data, message[12]))
        context.yy_dadishu.append((day_data, message[13]))
    # 查看是否有某天没有数据
    for key, value in context.items():
        date_list = []
        for t in value:
            date_list.append(str(t[0]))
        for i, e in enumerate(x_asix):
            if e not in date_list:
                value.insert(i, [e, 0])
        for i, j in enumerate(value):
            value[i] = int(j[1])
    d.context = context
    d.x_asix = x_asix

    return d


def day_range(begin_time, end_time):
    """
    功能:开始时间和结束时间之间的每天
    -------------------------------
    修改人            修改时间
    -------------------------------
    张栋梁            2018-10-17
    :param begin_time:
    :param end_time:
    :return:
    """
    dates = []
    dt = datetime.datetime.strptime(begin_time, "%Y%m%d")
    date = begin_time[:]
    while date <= end_time:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y%m%d")
    return dates


def month_range(begin_time, end_time):
    """
    功能:开始时间和结束时间之间的每月
    -------------------------------
    修改人            修改时间
    -------------------------------
    张栋梁            2018-10-17
    :param begin_time:
    :param end_time:
    :return:
    """
    month_set = set()
    for date in day_range(begin_time, end_time):
        month_set.add(date[0:6])
    month_list = []
    for month in month_set:
        month_list.append(month)
    return sorted(month_list)