from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, T, price, vat_cents, tax1, tax2, tax3')


def vat_cents(n):
    return round(n * 14 / 100)


pyDatalog.create_terms('vat_cents')          # named after the def
+price('pen', 300)

tax1(X, T) <= price(X, N) & (T == vat_cents(N))
tax2(X, T) <= (T == vat_cents(N)) & price(X, N)      # call before fill
tax3(X, vat_cents(N)) <= price(X, N)                 # call in the head
print(sorted(tax1(X, T).data))
print(sorted(tax2(X, T).data))
print(sorted(tax3(X, T).data))
