from pyDatalog import pyDatalog

pyDatalog.create_terms('O, I, Q, P, C, price, bought, line')

priced = {'pen': 300, 'book': 1200, 'lamp': 1999, 'mug': 450}  # the CSV
orders = [(1, 'pen', 3), (1, 'book', 1), (2, 'lamp', 2), (2, 'mug', 1),
          (3, 'kettle', 1)]            # order 3 asks for a new item

for item, cents in priced.items():
    +price(item, cents)
for o, item, qty in orders:
    +bought(o, item, qty)

line(O, I, C) <= bought(O, I, Q) & price(I, P) & (C == Q * P)
print('lines of order 3:', line(3, I, C).data)

# the rule is silent about what it could not price; Python can check
ordered = {item for o, item, qty in orders}
print('items with no price:', sorted(ordered - set(priced)))
