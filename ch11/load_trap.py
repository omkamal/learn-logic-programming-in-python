import csv, json
from pyDatalog import pyDatalog

pyDatalog.create_terms('O, I, Q, P, C, price, bought, line')

with open('prices.csv', newline='') as f:
    rows = list(csv.DictReader(f))
print(rows[0])

for r in rows:
    +price(r['item'], r['cents'])           # text, not a number
for o in json.load(open('orders.json')):
    +bought(o['order'], o['item'], o['qty'])

line(O, I, C) <= bought(O, I, Q) & price(I, P) & (C == Q * P)
for row in sorted(line(O, I, C).data):
    print(row)
