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

pyDatalog.create_terms('E, N, M, K, X, Y, reports_to, under')

# join through the NAME column: rows -> plain strings
reports_to(N, M) <= (Employee.name[E] == N) & (Employee.manager_name[E] == M) & (M != None)
under(N, M) <= reports_to(N, M)
under(N, M) <= reports_to(N, K) & under(K, M)

print(sorted(under('cid', M).data))
print(sorted(under(N, 'bob').data))
# plain SQL-backed comparison query
print(sorted(r[0].name for r in (Employee.salary[X] > 85).data))
