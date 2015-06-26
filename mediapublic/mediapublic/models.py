from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension(), expire_on_commit=False))
Base = declarative_base()

class CreationMixin():

    @classmethod
    def add(cls, **kwargs):
        with transaction.manager:
            thing = cls(**kwargs)
            DBSession.add(thing)
            transaction.commit()
        return thing

    @classmethod
    def get_all(cls):
        with transaction.manager:
            things = DBSession.query(
                cls,
            ).all()
            retThings = []
            for t in things:
                retThings.append(t.to_dict())
        return retThings

    @classmethod
    def get_by_id(cls, id):
        with transaction.manager:
            thing = DBSession.query(
                cls,
            ).filter(
                cls.id == id,
            ).first()
        return thing

    @classmethod
    def delete_by_id(cls, id):
        with transaction.manager:
            thing = cls.get_by_id(id)
            DBSession.delete(thing)
            transaction.commit()
        return thing

    @classmethod
    def update_by_id(cls, id, *args, **kargs):
        with transaction.manager:
             thing = cls.get_by_id(id)
             # TODO: magic
             DBSession.add(thing)
             transaction.commit()
        return thing

class Users(Base, CreationMixin):

    __tablename__ = 'users'



'''
class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)
'''


