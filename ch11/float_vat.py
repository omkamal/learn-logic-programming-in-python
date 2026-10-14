from pyDatalog import pyDatalog

def vat(amount):                # the shop with dollars, as decimal numbers
    return round(amount * 0.14, 2)

print('Python alone:', vat(12))

pyDatalog.create_terms('X, N, T, price, tax, vat')

+price('pen', 3)
+price('book', 12)
tax(X, T) <= price(X, N) & (T == vat(N))

print('in a rule:', sorted(tax(X, T).data))
