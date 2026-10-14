import textwrap
from shop_model import Product, Supplier
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, P, S, C, made_bad, made_ok, Y')

# the bug: S is a plain string, but Supplier.city[S] wants a Supplier
made_bad(P, C) <= ((Product.name[X] == P) &
                   (Product.supplier_name[X] == S) &
                   (Supplier.city[S] == C))
try:
    print(made_bad(P, C).data)
except Exception as e:
    print(textwrap.fill('%s: %s' % (type(e).__name__, e), 70,
                        subsequent_indent='    '))

# the fix: find the Supplier by its NAME, then read its city
made_ok(P, C) <= ((Product.name[X] == P) &
                  (Product.supplier_name[X] == S) & (S != None) &
                  (Supplier.name[Y] == S) & (Supplier.city[Y] == C))
print(sorted(made_ok(P, C).data))
