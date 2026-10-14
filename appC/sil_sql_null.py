from sqlalchemy import create_engine, Column, String
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
    manager_name = Column(String)           # NULL for the top person


Base.metadata.create_all(engine)
session.add_all([Employee(name='ann', manager_name=None),
                 Employee(name='bob', manager_name='ann')])
session.commit()

pyDatalog.create_terms('E, N, M, pairs, pairs_ok')
pairs(N, M) <= (Employee.name[E] == N) & (Employee.manager_name[E] == M)
pairs_ok(N, M) <= pairs(N, M) & (M != None)
print(sorted(pairs(N, M).data, key=str))
print(sorted(pairs_ok(N, M).data))
