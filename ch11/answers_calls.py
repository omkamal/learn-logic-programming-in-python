from pyDatalog import pyDatalog

calls = []

def vat_cents(cents):
    calls.append(cents)
    return round(cents * 14 / 100)

pyDatalog.create_terms('X, N, T, price, tax, vat_cents')

for item, cents in [('pen', 300), ('book', 1200),
                    ('lamp', 1999), ('mug', 450)]:
    +price(item, cents)
tax(X, T) <= price(X, N) & (T == vat_cents(N))

tax(X, T).data
tax(X, T).data
tax('mug', T).data
print(len(calls))
