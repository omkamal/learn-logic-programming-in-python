from pyDatalog import pyDatalog

def vat(amount):
    return round(amount * 0.14, 2)
half = lambda n: n / 2

pyDatalog.create_terms('X, N, T, price, tax, cost, half')   # vat is NOT listed
+price('book', 12)

# trap 1: vat was not passed to create_terms, so Python calls it right now, on N itself
try:
    tax(X, T) <= price(X, N) & (T == vat(N))
except TypeError as e:
    print('TypeError:', e)

# trap 2: a lambda passed to create_terms
cost(X, T) <= price(X, N) & (T == half(N))
print(sorted(cost(X, T).data))
