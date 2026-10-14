from sqlalchemy import event
from shop_model import Product, Supplier, engine, session
from pyDatalog import pyDatalog

@event.listens_for(engine, 'before_cursor_execute')
def show(conn, cursor, statement, params, context, executemany):
    text = ' '.join(statement.split())
    print('   ', 'FROM ' + text.split(' FROM ')[1] if ' FROM ' in text
          else text, params)

pyDatalog.create_terms('X, Y, P, S, C, made_in')

# two tables, joined through the supplier NAME
made_in(P, C) <= ((Product.name[X] == P) &
                  (Product.supplier_name[X] == S) & (S != None) &
                  (Supplier.name[Y] == S) & (Supplier.city[Y] == C))

print(sorted(made_in(P, C).data))

# what if acme moves? change the row, then ask again
session.get(Supplier, 'acme').city = 'giza'
session.commit()
print(sorted(made_in(P, C).data))
