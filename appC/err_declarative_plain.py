from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from pyDatalog import pyDatalog

engine = create_engine('sqlite://')
session = sessionmaker(bind=engine)()
pyDatalog.create_terms('X')

Base = declarative_base()          # plain: no Mixin, no sqlMetaMixin
Base.session = session


class Cat(Base):
    __tablename__ = 'cat'
    name = Column(String, primary_key=True)
    age = Column(Integer)


Base.metadata.create_all(engine)
session.add(Cat(name='tom', age=5))
session.commit()

try:
    print((Cat.age[X] > 1).data)
except Exception as err:
    print(type(err).__name__ + ':', err)
