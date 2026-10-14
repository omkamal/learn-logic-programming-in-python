from pyDatalog import pyDatalog

def shipping(grams):
    """Fee in cents: three weight bands, plain Python if / else."""
    if grams <= 500:
        return 400
    if grams <= 2000:
        return 750
    return 1500

print(shipping(120), shipping(1800), shipping(5000))

pyDatalog.create_terms('X, G, C, weight, fee, shipping')

+weight('pen', 20)
+weight('book', 900)
+weight('lamp', 2500)

fee(X, C) <= weight(X, G) & (C == shipping(G))
print(sorted(fee(X, C).data))
