from pyDatalog import pyDatalog

def vat_cents(cents):
    return round(cents * 14 / 100)

pyDatalog.create_terms('X, N, T, price, early, in_head, vat_cents')

+price('pen', 300)
+price('book', 1200)

# 1. the call written before the literal that fills N
early(X, T) <= (T == vat_cents(N)) & price(X, N)
print(early(X, T).data)

# 2. the call written in the head of the clause
in_head(X, vat_cents(N)) <= price(X, N)
print(in_head(X, T).data)
