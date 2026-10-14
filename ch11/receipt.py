import csv, json
from pyDatalog import pyDatalog

def vat_cents(cents):
    return round(cents * 14 / 100)

def money(cents):
    return '%d.%02d' % (cents // 100, cents % 100)

pyDatalog.create_terms('O, I, Q, P, C, V, S, T, D')
pyDatalog.create_terms('price, bought, vat_cents')
pyDatalog.create_terms('line, vat, subtotal, tax_total, due')

# the facts come from two files
with open('prices.csv', newline='') as f:
    for r in csv.DictReader(f):
        +price(r['item'], int(r['cents']))
for o in json.load(open('orders.json')):
    +bought(o['order'], o['item'], o['qty'])

# the rules: one line per item bought, its VAT, then totals per order
line(O, I, C) <= bought(O, I, Q) & price(I, P) & (C == Q * P)
vat(O, I, V) <= line(O, I, C) & (V == vat_cents(C))
(subtotal[O] == sum_(C, for_each=I)) <= line(O, I, C)
(tax_total[O] == sum_(V, for_each=I)) <= vat(O, I, V)
due(O, D) <= (subtotal[O] == S) & (tax_total[O] == T) & (D == S + T)

# the receipts: format for people only now
for o, d in sorted(due(O, D).data):
    print('order', o)
    for item, c in sorted(line(o, I, C).data):
        print('  %-5s %7s' % (item, money(c)))
    print('  tax   %7s' % money((tax_total[o] == T).data[0][0]))
    print('  DUE   %7s' % money(d))
