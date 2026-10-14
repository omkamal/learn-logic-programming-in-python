from pyDatalog import pyDatalog

calls = []

def vat_cents(cents):
    calls.append(cents)
    return round(cents * 14 / 100)

pyDatalog.create_terms('X, N, T, price, fixed, vat_cents')

+price('pen', 300)
+price('book', 1200)

# the argument is a plain number: there is no blank to wait for
fixed(X, T) <= price(X, N) & (T == vat_cents(1000))
print('after writing the rule:', len(calls))

print(sorted(fixed(X, T).data))
print(sorted(fixed(X, T).data))
print('after two queries:', len(calls))
