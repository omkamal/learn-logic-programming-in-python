from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, T, price, tax_floor, tax')

# prices in whole cents: pen 3.00, book 12.00, lamp 19.99
+price('pen', 300)
+price('book', 1200)
+price('lamp', 1999)

# arithmetic is fine, but // always rounds DOWN, and the shop rounds to
# the nearest cent
tax_floor(X, T) <= price(X, N) & (T == N * 14 // 100)
print(sorted(tax_floor(X, T).data))

# so a Python programmer reaches for round()
try:
    tax(X, T) <= price(X, N) & (T == round(N * 14 / 100))
except TypeError as e:
    print('TypeError:', e)
