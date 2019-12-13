from es_demo.common import ElasticSearchClass
from sql_common import db
import operator

obj = ElasticSearchClass("192.168.99.107", "9200", "", "")


class public_Compare:

    def __init__(self, index_name):
        self.index_name = index_name
        self.rule_data = index_name

    def compare_loft(self):
        pass

    def compare_stair(self):
        pass

    def compare_exit(self):
        pass