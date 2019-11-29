from elasticsearch import Elasticsearch


class ElasticSearchClass(object):

    def __init__(self, host, port, user, passwrod):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwrod
        self.connect()

    def connect(self):
        """客户端的连接"""
        self.es = Elasticsearch(hosts=[{'host': self.host, 'port': self.port}],
                                http_auth=(self.user, self.password))

    def insertDocument(self, index, type, body, id=None):
        '''
        插入一条数据body到指定的index、指定的type下;可指定Id,若不指定,ES会自动生成
        :param index: 待插入的index值
        :param type: 待插入的type值
        :param body: 待插入的数据 -> dict型
        :param id: 自定义Id值
        :return:
        '''
        return self.es.index(index=index, doc_type=type, body=body, id=id)

    def count(self, indexname):
        """
        :param indexname:
        :return: 统计index总数
        """
        return self.conn.count(index=indexname)

    def delete(self, indexname, doc_type, id):
        """
        :param indexname:
        :param doc_type:
        :param id:
        :return: 删除index中具体的一条
        """
        self.es.delete(index=indexname, doc_type=doc_type, id=id)

    def get(self, doc_type, indexname, id):
        return self.es.get(index=indexname, doc_type=doc_type, id=id)

    def searchindex(self, index):
        """
        查找所有index数据
        """
        try:
            return self.es.search(index=index)
        except Exception as err:
            print(err)

    def searchDoc(self, index=None, type=None, body=None):
        '''
        查找index下所有符合条件的数据
        :param index:
        :param type:
        :param body: 筛选语句,符合DSL语法格式
        :return:
        '''
        return self.es.search(index=index, doc_type=type, body=body)

    def search(self, index, body):
        """
        根据index，type查找数据，
        其中size默认为十条数据，可以修改为其他数字，但是不能大于10000
        """
        # search(self, index=None, body=None, params=None)
        print("body", body)
        return self.es.search(index=index, body=body, doc_type="text")

    def scroll(self, scroll_id, scroll):
        """
        根据上一个查询方法，查询出来剩下所有相关数据
        """
        return self.es.scroll(scroll_id=scroll_id, scroll=scroll)
