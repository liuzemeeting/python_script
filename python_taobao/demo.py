import requests


if __name__ == "__main__":
    # 获取淘宝信息数据
    url = "http://api.tbk.dingdanxia.com/tbk/super_search"
    data = {"apikey": "IjLS35sJYEhun3oyE9Up9KdlFL5mNYPd", "q": "男装", "page_no": 1}
    response_data = requests.post(url, data=data)
    good_data = response_data.json()["data"]
    for i in good_data:
        print(i)
    # 获取订单数据
    # url = "http://api.tbk.dingdanxia.com/tbk/order_details"
    # data = {"apikey": "IjLS35sJYEhun3oyE9Up9KdlFL5mNYPd",
    #         "start_time": "2019-08-03 10:53:11",
    #         "end_time": "2019-08-03 12:53:11"}
    # response_data = requests.post(url, data=data)
    # print(response_data.json())
    # order_data = response_data.json()["data"]
    # for i in order_data:
    #     print(i)
    # url = "https://pub.alimama.com/cp/event/list.json?toPage=1&perPageSize=40&sceneId=6&t=1572598697640&_tb_token_=7563a0fee7713&pvid="
    # response_data = requests.post(url)
    # print(response_data.content)
