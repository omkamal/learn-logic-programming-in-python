from pyDatalog import pyDatalog

pyDatalog.create_terms('N, T, price, tax')
+price('pen', 300)


def vat_cents(n):
    return round(n * 14 / 100)


try:
    # vat_cents was never named in create_terms
    tax(N, T) <= price('pen', N) & (T == vat_cents(N))
except Exception as err:
    print(type(err).__name__ + ':', err)
