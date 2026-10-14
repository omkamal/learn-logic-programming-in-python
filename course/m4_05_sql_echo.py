from sqlalchemy import create_engine, event, Column, Integer, String, ForeignKey
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
pyDatalog.create_terms('X')

# print every SQL statement the database receives from now on
@event.listens_for(engine, 'before_cursor_execute')
def show(conn, cursor, statement, params, context, executemany):
    print('SQL:', ' '.join(statement.split()), params)

rows = (Employee.salary[X] > 85).data
print(type(rows[0][0]).__name__, sorted(r[0].name for r in rows))
