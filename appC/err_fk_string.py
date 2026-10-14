import textwrap
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from pyDatalog import pyDatalog

engine = create_engine('sqlite://')
session = sessionmaker(bind=engine)()
Base = declarative_base(cls=pyDatalog.Mixin,
                        metaclass=pyDatalog.sqlMetaMixin)
Base.session = session


class Employee(Base):
    __tablename__ = 'employee'
    name = Column(String, primary_key=True)
    manager_name = Column(String)         # a foreign key: holds a string
    salary = Column(Integer)


Base.metadata.create_all(engine)
session.add_all([Employee(name='ann', manager_name=None, salary=150),
                 Employee(name='bob', manager_name='ann', salary=100),
                 Employee(name='cid', manager_name='bob', salary=80)])
session.commit()

pyDatalog.create_terms('X, Y, Z, above')
above(X, Y) <= (Employee.manager_name[X] == Y)
above(X, Y) <= (Employee.manager_name[X] == Z) & above(Z, Y)
try:
    print(above(X, Y).data)
except Exception as err:
    print(textwrap.fill(type(err).__name__ + ': ' + str(err), 70,
                        subsequent_indent='    '))
try:
    print((Employee.manager_name['bob'] == Y).data)
except Exception as err:
    print(type(err).__name__ + ':', err)
