from shop_model import Product, Supplier
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, S, C')

# an attribute defined by a clause that mixes TWO mapped classes
(Product.city[X] == C) <= ((Product.supplier_name[X] == S) &
                           (Supplier.name[Y] == S) &
                           (Supplier.city[Y] == C))
print((Product.city[X] == C).data)
print([r[0].city for r in (Product.name[X] == 'pen').data])
