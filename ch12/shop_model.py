from sqlalchemy import Column, Integer, String, ForeignKey
from model import Base, engine, session

class Supplier(Base):
    __tablename__ = 'supplier'
    name = Column(String, primary_key=True)
    city = Column(String)

class Product(Base):
    __tablename__ = 'product'
    name = Column(String, primary_key=True)
    supplier_name = Column(String, ForeignKey('supplier.name'))
    cents = Column(Integer)

Base.metadata.create_all(engine)
session.add_all([Supplier(name='acme', city='cairo'),
                 Supplier(name='bolt', city='dubai'),
                 Supplier(name='cedar', city='london'),
                 Product(name='pen', supplier_name='acme', cents=300),
                 Product(name='book', supplier_name='bolt', cents=1200),
                 Product(name='lamp', supplier_name='acme', cents=1999),
                 Product(name='desk', supplier_name='bolt', cents=8900),
                 Product(name='mug', supplier_name=None, cents=450)])
session.commit()
