from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from pyDatalog import pyDatalog

engine = create_engine('sqlite://')
session = sessionmaker(bind=engine)()
pyDatalog.create_terms('X')

Base = declarative_base(cls=pyDatalog.Mixin,
                        metaclass=pyDatalog.sqlMetaMixin)
# Base.session = session   <- the line that is missing


class Pet(Base):
    __tablename__ = 'pet'
    name = Column(String, primary_key=True)
    age = Column(Integer)


Base.metadata.create_all(engine)
session.add(Pet(name='rex', age=3))
session.commit()

print((Pet.age[X] > 1).data)
Base.session = session
print(len((Pet.age[X] > 1).data), 'row once the session is set')
