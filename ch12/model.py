from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from pyDatalog import pyDatalog

engine = create_engine('sqlite://')         # an in-memory database
session = sessionmaker(bind=engine)()       # a session on that engine
Base = declarative_base(cls=pyDatalog.Mixin,
                        metaclass=pyDatalog.sqlMetaMixin)
Base.session = session                      # logic queries use this session

class Employee(Base):
    __tablename__ = 'employee'
    name = Column(String, primary_key=True)
    manager_name = Column(String, ForeignKey('employee.name'))
    salary = Column(Integer)
    def __repr__(self):
        return 'Employee(%s)' % self.name

Base.metadata.create_all(engine)
session.add_all([Employee(name='ann', manager_name=None,  salary=150),
                 Employee(name='bob', manager_name='ann', salary=100),
                 Employee(name='cid', manager_name='bob', salary=80),
                 Employee(name='dee', manager_name='bob', salary=90)])
session.commit()
