# coding=utf-8
# @Time    : 2018/10/22 下午3:24


from sqlalchemy.orm import class_mapper
from application import db


def db_session_commit():
    try:
        db.session.commit()
    except Exception:
        print('db_session_commitdb_session_commit')
        db.session.rollback()
        raise


class CRUDMixin(object):
    def __repr__(self):
        return "<{}>".format(self.__class__.__name__)

    def add(self, commit=False):
        db.session.add(self)
        commit and db_session_commit()

    def create(self, commit=False, **kwargs):
        """
        根据parser解析的dict form字段，自动填充相应字段
        :param commit:  是否提交，默认为False
        :param kwargs: 创建模型关联的字典值
        :return self or False: 若commit为False， 则返回false;反之且提交成功，则返回self
        """
        for attr, value in kwargs.items():
            if value is not None and hasattr(self, attr):
                setattr(self, attr, value)
        return self.save(commit=commit)

    def update(self, commit=False, **kwargs):
        """
        更新已有实体的一些提交字段（排除id）
        :param commit: 是否提交，默认提交
        :param kwargs:  参数值
        :return self or False: 若commit为False， 则返回false;反之且提交成功，则返回self
        """
        kwargs.pop("id", None)
        for attr, value in kwargs.items():
            # Flask-RESTful make everything None by default: /
            if value is not None and hasattr(self, attr):
                setattr(self, attr, value)
        return commit and self.save(commit=commit) or self

    def save(self, commit=False):
        """
        保存对象到数据库中，持久化对象
        :param commit: 是否提交，默认提交
        :return self or False: 若commit为False， 则返回false;反之且提交成功，则返回self
        """
        db.session.add(self)
        db.session.flush()
        commit and db_session_commit()
        return self

    def delete(self, commit=False):
        """
        删除对象，从数据库中删除记录
        :param commit: 是否提交，默认提交
        :return self or False: 若commit为False， 则返回false;反之且提交成功，则返回self
        """
        db.session.delete(self)
        commit and db_session_commit()
        return self

    @classmethod
    def upsert(cls, where, commit=False, **kwargs):
        record = cls.query.filter_by(**where).first()
        print('record', record, where)
        if record:
            record.update(commit=commit, **kwargs)
        else:
            record = cls(**kwargs).save(commit=commit)
        return record

    def to_json(self):
        if hasattr(self, '__table__'):
            return {i.name: getattr(self, i.name) for i in self.__table__.columns}
        raise AssertionError('<%r> does not have attribute for __table__' % self)


def model_to_dict(obj, visited_children=None, back_relationships=None):
    """
    说明：实例模型转化为字典，只转当前对象及直接父对象
    ----------------------------------------
    修改人          修改日期          修改原因
    ----------------------------------------
    Zuyong Du         2018-10-22
    ----------------------------------------
    杜祖永 2018-08-30
    ----------------------------------------
    """
    if visited_children is None:
        visited_children = set()
    if back_relationships is None:
        back_relationships = set()
    serialized_data = {c.key: getattr(obj, c.key) for c in obj.__table__.columns}
    print(serialized_data)
    relationships = class_mapper(obj.__class__).relationships
    visitable_relationships = [(name, rel) for name, rel in relationships.items() if name not in back_relationships]
    for name, relation in visitable_relationships:
        relationship_children = getattr(obj, name)
        if relationship_children is not None:
            if relation.uselist:
                children = []
                # for child in [c for c in relationship_children if c not in visited_children]:
                #     visited_children.add(child)
                #     children.append(model_to_dict(child, visited_children, back_relationships))
                # serialized_data[name] = children
            else:
                serialized_data[name] = {c.key: getattr(relationship_children, c.key) for c in
                                         relationship_children.__table__.columns}
    return serialized_data
