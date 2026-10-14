from sqlalchemy import Column, Integer, String
from model import Base, engine, session

class Film(Base):
    __tablename__ = 'film'
    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(Integer)
    minutes = Column(Integer)

films = [('Lantern Season', 'ines', 1994, 112),
         ('The Copper Tide', 'omar', 1998, 131),
         ('Seven Quiet Doors', 'ines', 2001, 95),
         ('Orchard of Clocks', 'lena', 2003, 88),
         ('A Map for Rain', 'kofi', 2005, 104),
         ('Tin Kingdom', 'lena', 2008, 97),
         ('Salt and Static', 'omar', 2011, 118),
         ('The Long Thaw', 'ines', 2014, 92),
         ('Blue Hour Club', 'ines', 2016, 101),
         ('Paper Weather', 'lena', 2019, 86),
         ('Harbor of Small Lies', 'omar', 2021, 99),
         ('Echo Garden', 'kofi', 2023, 107)]

Base.metadata.create_all(engine)
session.add_all([Film(title=t, director=d, year=y, minutes=m)
                 for t, d, y, m in films])
session.commit()
