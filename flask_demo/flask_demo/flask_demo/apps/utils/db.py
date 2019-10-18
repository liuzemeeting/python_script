# !/usr/bin/python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 11:11
# @Author  : hshen
"""
sqlalchmy 查询的的数据进行返回
"""
from decimal import Decimal

from sqlalchemy.orm import class_mapper
import redis
import py2neo


class CRUDMixin(object):
    def __repr__(self):
        return "<{}>".format(self.__class__.__name__)

    def to_json(self):
        if hasattr(self, '__table__'):
            data = {}
            for i in self.__table__.columns:
                value = getattr(self, i.name)
                if isinstance(value, Decimal):
                    value = str(value)
                data[i.name] = value
            return data

        raise AssertionError('<%r> does not have attribute for __table__' % self)


def model_to_dict(obj, visited_children=None, back_relationships=None):
    """
    实例模型转化为字典，只转当前对象及直接父对象
    url：
    """
    if visited_children is None:
        visited_children = set()
    if back_relationships is None:
        back_relationships = set()
    serialized_data = {}
    for c in obj.__table__.columns:
        value = getattr(obj, c.key)
        if isinstance(value, Decimal):
            value = str(value)
        serialized_data[c.key] = value

    relationships = class_mapper(obj.__class__).relationships
    visitable_relationships = [(name, rel) for name, rel in relationships.items() if name not in back_relationships]
    for name, relation in visitable_relationships:
        relationship_children = getattr(obj, name)
        if relationship_children is not None:
            if relation.uselist:
                children = []
                for child in [c for c in relationship_children if c not in visited_children]:
                    visited_children.add(child)
                    children.append(model_to_dict(child, visited_children, back_relationships))
                serialized_data[name] = children
            else:
                serialized_data[name] = {}
                for c in relationship_children.__table__.columns:
                    value = getattr(relationship_children, c.key)
                    if isinstance(value, Decimal):
                        value = str(value)
                    serialized_data[name][c.key] = value
    return serialized_data




class Struct(dict):
    """
    - 为字典加上点语法. 例如:
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


# mysql


# neo4j
def py2neo_id(self):
    return py2neo.remote(self)._id


py2neo.types.Node._id = property(py2neo_id)
py2neo.types.Relationship._id = property(py2neo_id)


class NeoHub:

    def __init__(self):
        self._driver = None

    @property
    def driver(self):
        if not self._driver:
            self._driver = py2neo.Graph("http://192.168.99.100:7474",
                                        user="neo4j", password="123456")
        return self._driver

    def run(self, statement, args=None, **kwargs):
        """
        :return: first value from the first record returned or
                 :py:const:`None`.
        """
        return self.driver.evaluate(statement, args, **kwargs)

    def fetchall(self, statement, args=None, **kwargs):
        rows = self.driver.data(statement, args, **kwargs)
        return rows

    def fetchone(self, statement, args=None, **kwargs):
        rows = self.fetchall(statement, args, **kwargs)
        return rows[0] if rows else None

    def begin(self, autocommit=False):
        """ Begin a new :class:`.Transaction`.

        :param autocommit: if :py:const:`True`, the transaction will
                         automatically commit after the first operation
        """
        return self.driver.begin(autocommit)


neo = NeoHub()

# redis
rdsc = redis.StrictRedis(
    host="127.0.0.1",
    port="6379",
    db=1
)


class RedisHub:
    DEFAULT_TIMEOUT = 3600 * 4

    def __init__(self):
        # {prefix: timeout}
        self._prefixd = {}

    def __getattr__(self, prefix):
        timeout = self.DEFAULT_TIMEOUT
        return RedisProxy(prefix, timeout)


def struct(data):
    if isinstance(data, list):
        data = [struct(row) for row in data]
    if isinstance(data, dict):
        for k, v in data.iteritems():
            data[k] = struct(v)
        data = Struct(data)
    return data


import json, pickle
class RedisProxy:

    def __init__(self, prefix, timeout):
        self.prefix = prefix
        self.timeout = timeout

    def genkey(self, arg):
        if not arg:
            return self.prefix
        args = json.dumps(arg)
        key = self.prefix + '_' + args
        return key

    def encodev(self, v):
        return pickle.dumps(v)

    def decodev(self, data):
        return pickle.loads(data)

    def get(self, arg=None):
        key = self.genkey(arg)
        data = rdsc.get(key)
        if not data:
            return data
        return self.decodev(data)

    def set(self, arg, val):
        key = self.genkey(arg)
        val = self.encodev(val)
        return rdsc.set(key, val, self.timeout)

    def delete(self, *args):
        args = [self.genkey(arg) for arg in args]
        return rdsc.delete(*args)


rds = RedisHub()
