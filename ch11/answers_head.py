from pyDatalog import pyDatalog

def dollars(cents):
    return cents / 100

pyDatalog.create_terms('X, N, D, price, shown_bad, shown, dollars')

+price('pen', 300)
+price('book', 1200)

shown_bad(X, dollars(N)) <= price(X, N)      # the call sits in the head
print(shown_bad(X, D).data)

shown(X, D) <= price(X, N) & (D == dollars(N))
print(sorted(shown(X, D).data))
