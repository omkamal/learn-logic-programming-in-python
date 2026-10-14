from pyDatalog import pyDatalog

pyDatalog.create_terms('N, T, price, tax, vat_cents')    # named too early
+price('pen', 300)


def vat_cents(n):                  # the def replaces the term
    return round(n * 14 / 100)


try:
    tax(N, T) <= price('pen', N) & (T == vat_cents(N))
except Exception as err:
    print(type(err).__name__ + ':', err)
