from sqlalchemy import create_engine, event, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from pyDatalog import pyDatalog

engine = create_engine('sqlite://')
session = sessionmaker(bind=engine)()
Base = declarative_base(cls=pyDatalog.Mixin,
                        metaclass=pyDatalog.sqlMetaMixin)
Base.session = session

class Employee(Base):
    __tablename__ = 'employee'
    name = Column(String, primary_key=True)
    manager_name = Column(String, ForeignKey('employee.name'))
    salary = Column(Integer)
    manager = relationship('Employee', remote_side=[name])  # an object
    def __repr__(self):
        return 'Employee(%s)' % self.name

Base.metadata.create_all(engine)
session.add_all([Employee(name='ann', manager_name=None,  salary=150),
                 Employee(name='bob', manager_name='ann', salary=100),
                 Employee(name='cid', manager_name='bob', salary=80),
                 Employee(name='dee', manager_name='bob', salary=90)])
session.commit()

@event.listens_for(engine, 'before_cursor_execute')
def show(conn, cursor, statement, params, context, executemany):
    print('SQL statement sent')

pyDatalog.create_terms('X, Y, Z, above')
above(X, Y) <= (Employee.manager[X] == Y) & (Y != None)
above(X, Y) <= (Employee.manager[X] == Z) & above(Z, Y)
for x, y in sorted(above(X, Y).data, key=str):
    print(x, 'is below', y)
