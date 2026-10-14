import csv, json
from pyDatalog import pyDatalog

# no create_terms needed: assert_fact takes the predicate name as text
with open('prices.csv', newline='') as f:
    for r in csv.DictReader(f):
        pyDatalog.assert_fact('price', r['item'], int(r['cents']))

for o in json.load(open('orders.json')):
    pyDatalog.assert_fact('bought', o['order'], o['item'], o['qty'])

pyDatalog.create_terms('O, I, Q, P, C, price, bought, line')
line(O, I, C) <= bought(O, I, Q) & price(I, P) & (C == Q * P)
for row in sorted(line(O, I, C).data):
    print(row)
