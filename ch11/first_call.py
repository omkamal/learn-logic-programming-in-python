from pyDatalog import pyDatalog

# step 1: an ordinary Python function, written and tested on its own
def vat_cents(cents):
    """VAT at 14 percent, rounded to the nearest whole cent."""
    return round(cents * 14 / 100)

print(vat_cents(300), vat_cents(1999))

# step 2: only now tell pyDatalog that vat_cents is a function to call
pyDatalog.create_terms('X, N, T, G, price, tax, gross, vat_cents')

+price('pen', 300)
+price('book', 1200)
+price('lamp', 1999)

# step 3: use it in a rule, like any other literal
tax(X, T) <= price(X, N) & (T == vat_cents(N))
gross(X, G) <= price(X, N) & tax(X, T) & (G == N + T)

print(sorted(tax(X, T).data))
print(sorted(gross(X, G).data))
