from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from pyDatalog import pyDatalog

engine = create_engine('sqlite://')
session = sessionmaker(bind=engine)()
pyDatalog.create_terms('X')

# slip 1: the right base class, but Base.session = session is missing
Base = declarative_base(cls=pyDatalog.Mixin,
                        metaclass=pyDatalog.sqlMetaMixin)

class Pet(Base):
    __tablename__ = 'pet'
    name = Column(String, primary_key=True)
    age = Column(Integer)

# slip 2: a plain base class, without the Mixin and the metaclass
PlainBase = declarative_base()

class Cat(PlainBase):
    __tablename__ = 'cat'
    name = Column(String, primary_key=True)
    age = Column(Integer)

Base.metadata.create_all(engine)
PlainBase.metadata.create_all(engine)
session.add_all([Pet(name='rex', age=3), Cat(name='tom', age=5)])
session.commit()

print((Pet.age[X] > 1).data)
try:
    print((Cat.age[X] > 1).data)
except AttributeError as e:
    print('AttributeError:', e)
