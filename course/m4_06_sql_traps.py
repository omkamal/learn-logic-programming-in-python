from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from pyDatalog import pyDatalog

engine = create_engine('sqlite://')
session = sessionmaker(bind=engine)()
Base = declarative_base(cls=pyDatalog.Mixin, metaclass=pyDatalog.sqlMetaMixin)
Base.session = session

class Employee(Base):
    __tablename__ = 'employee'
    name = Column(String, primary_key=True)
    manager_name = Column(String, ForeignKey('employee.name'))
    salary = Column(Integer)

Base.metadata.create_all(engine)
session.add_all([Employee(name='ann', manager_name=None,  salary=150),
                 Employee(name='bob', manager_name='ann', salary=100),
                 Employee(name='cid', manager_name='bob', salary=80),
                 Employee(name='dee', manager_name='bob', salary=90)])
session.commit()
pyDatalog.create_terms('E, N, M, X, Y, Z, above, reports_to')

# trap 1: recurse straight through the foreign-key column
above(X, Y) <= (Employee.manager_name[X] == Y)
above(X, Y) <= (Employee.manager_name[X] == Z) & above(Z, Y)
try:
    print(above(X, Y).data)
except AttributeError as e:
    print('AttributeError:', e)

# the same mistake, asked directly: a string is not an Employee
try:
    print((Employee.manager_name['bob'] == Y).data)
except TypeError as e:
    print('TypeError:', e)

# trap 2: the name join without a None filter
reports_to(N, M) <= (Employee.name[E] == N) & (Employee.manager_name[E] == M)
print(sorted(reports_to(N, M).data))
