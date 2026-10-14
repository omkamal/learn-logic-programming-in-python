import math
from pyDatalog import pyDatalog

# 1. a plain Python function inside a clause
def vat(amount):
    return round(amount * 0.14, 2)

def double(p):
    return p * 2

# create_terms AFTER the def wraps the function, so it runs at query time on real values
pyDatalog.create_terms('X, Y, Z, N, T, price, tax, gross, root, items, emp, team, vat, double, math.sqrt')

+price('pen', 3)
+price('book', 12)
tax(X, T) <= price(X, N) & (T == vat(N))
print(sorted(tax(X, T).data))

root(X, Y) <= price(X, N) & (Y == math.sqrt(N))
print(sorted((a, round(b, 3)) for a, b in root(X, Y).data))

gross(X, Y) <= price(X, N) & (Y == double(N))
print(sorted(gross(X, Y).data))

# 2. tuple_ : collect values into a tuple
for n, t in [('ann', 'red'), ('bob', 'red'), ('cid', 'blue')]:
    +team(n, t)
(items[Y] == tuple_(X, order_by=X)) <= team(X, Y)
print(sorted(items[Y] == Z))

# 3. the program decorator: write clauses without worrying about Python name scope
@pyDatalog.program()
def _():
    +parent('a', 'b')
    +parent('b', 'c')
    anc(X, Y) <= parent(X, Y)
    anc(X, Y) <= anc(X, Z) & parent(Z, Y)
print(sorted(pyDatalog.ask("anc('a', Y)").answers))

# 4. load a block of datalog text, then query it
pyDatalog.clear()
pyDatalog.load("""
+ edge(1, 2)
+ edge(2, 3)
path(X, Y) <= edge(X, Y)
path(X, Y) <= path(X, Z) & edge(Z, Y)
""")
print(sorted(pyDatalog.ask("path(1, Y)").answers))
