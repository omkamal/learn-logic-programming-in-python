from pyDatalog import pyDatalog

def vat_a(cents):                    # defined, but never named below
    return round(cents * 14 / 100)

def twice(cents):                    # also never named, but only uses *
    return cents * 2

pyDatalog.create_terms('X, N, T, price, tax_a, tax_b, dbl, vat_b')

def vat_b(cents):                    # named BEFORE this def
    return round(cents * 14 / 100)

+price('pen', 300)
+price('book', 1200)

try:
    tax_a(X, T) <= price(X, N) & (T == vat_a(N))
except TypeError as e:
    print('A, never named:', e)
try:
    tax_b(X, T) <= price(X, N) & (T == vat_b(N))
except TypeError as e:
    print('B, named too early:', e)

dbl(X, T) <= price(X, N) & (T == twice(N))     # no error: just lucky
print('C, never named but lucky:', sorted(dbl(X, T).data))
