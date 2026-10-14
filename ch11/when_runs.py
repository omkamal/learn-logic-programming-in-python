from pyDatalog import pyDatalog

calls = []                      # the function notes down every call

def vat_cents(cents):
    calls.append(cents)
    return round(cents * 14 / 100)

pyDatalog.create_terms('X, N, T, price, tax, vat_cents')
+price('pen', 300)
+price('book', 1200)
+price('lamp', 1999)
print('after the facts:', len(calls))

tax(X, T) <= price(X, N) & (T == vat_cents(N))
print('after writing the rule:', len(calls))

print(sorted(tax(X, T).data))
print('after one query:', len(calls))
print(sorted(tax(X, T).data))
print('after the same query:', len(calls))
print(tax('book', T).data)
print('after asking for book:', len(calls))
print('arguments seen:', sorted(set(calls)), type(calls[0]).__name__)
