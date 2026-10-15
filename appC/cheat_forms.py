# Every form of Appendix B, run once (pyDatalog 0.22.4). Each block is
# labeled with the table of the appendix that shows it.
import math
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, V, C, P, T, S, M, K, A, B')
pyDatalog.create_terms('parent, grandparent, ancestor, sibling, price')
pyDatalog.create_terms('flight, reach, city, unreachable, big, double')
pyDatalog.create_terms('cost, dcost, factorial, fib, math.sqrt')
pyDatalog.create_terms('emp, total, headcount, top, who, names, items')
pyDatalog.create_terms('company, rnk, running, link, path, cheapest')
pyDatalog.create_terms('tax, root')


def vat_cents(n):                        # a plain function, defined first
    return round(n * 14 / 100)


pyDatalog.create_terms('vat_cents')      # ... and named afterwards

# --- facts: + and - ---------------------------------------------
+parent('alice', 'bob')
+parent('alice', 'carol')
+parent('bob', 'dave')
+parent('carol', 'erin')
+parent('zed', 'zoe')
-parent('zed', 'zoe')
pyDatalog.assert_fact('parent', 'erin', 'fay')
pyDatalog.retract_fact('parent', 'erin', 'fay')
+(cost['pen'] == 3)
+(cost['book'] == 12)
+(factorial[0] == 1)
+(fib[0] == 0)
+(fib[1] == 1)

# --- queries and answers -----------------------------------------
q = parent('alice', X)
print(type(q).__name__)                   # printing q shows a table
print(sorted(q.data))                     # a list of tuples
print(bool(parent('alice', 'bob')), parent('alice', 'bob').data)
print(parent('bob', 'alice').data)        # [] means no
print(sorted(pyDatalog.ask("parent('alice', X)").answers))
print(pyDatalog.ask("parent('zed', X)"))  # None
print((cost['pen'] == N).data, (cost[X] == 12).data)

# --- rules: <=, &, OR, ~, comparisons, calculations -------------
grandparent(X, Z) <= parent(X, Y) & parent(Y, Z)
sibling(X, Y) <= parent(P, X) & parent(P, Y) & (X != Y)
ancestor(X, Y) <= parent(X, Y)                       # base clause
ancestor(X, Y) <= ancestor(X, Z) & parent(Z, Y)      # recursive literal 1st
print(sorted(grandparent(X, Z).data))
print(sorted(sibling('bob', Y).data))
print(sorted(ancestor('alice', Y).data))

for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'CAI')]:
    +flight(a, b)
for c in ['CAI', 'DXB', 'LHR', 'NRT']:
    +city(c)
reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)
unreachable(Y) <= city(Y) & ~reach('CAI', Y)         # fill, then not
print(sorted(unreachable(Y).data))

+price('pen', 3)
+price('book', 12)
big(X) <= price(X, N) & (N > 5)                      # fill, then check
double(X, Y) <= price(X, N) & (Y == N * 2)           # fill, then compute
print(sorted(big(X).data), sorted(double(X, Y).data))

# --- functional notation ------------------------------------------
dcost[X] = cost[X] * 2
factorial[N] = N * factorial[N - 1]
fib[N] = fib[N - 1] + fib[N - 2]
print((dcost['book'] == V).data, (factorial[5] == V).data,
      (fib[20] == V).data)

# --- aggregates ----------------------------------------------------
for name, dept, pay in [('ann', 'eng', 120), ('bob', 'eng', 100),
                        ('cid', 'ops', 80), ('dee', 'ops', 90)]:
    +emp(name, dept, pay)
(total[Y] == sum_(N, for_each=X)) <= emp(X, Y, N)
(headcount[Y] == len_(X)) <= emp(X, Y, N)
(top[Y] == max_(N, order_by=N)) <= emp(X, Y, N)
(who[Y] == max_(X, order_by=N)) <= emp(X, Y, N)
(names[Y] == concat_(X, order_by=X, sep=', ')) <= emp(X, Y, N)
(items[Y] == tuple_(X, order_by=X)) <= emp(X, Y, N)
(company['all'] == sum_(N, for_each=X)) <= emp(X, Y, N)
(rnk[X] == rank_(group_by=Y, order_by=-N)) <= emp(X, Y, N)
(running[X] == running_sum_(N, group_by=Y, order_by=X)) <= emp(X, Y, N)
for t in (total, headcount, top, who, names, items, rnk, running):
    print(sorted((t[X] == V).data))
print((company['all'] == V).data)

for a, b, c in [('CAI', 'DXB', 4), ('DXB', 'LHR', 7), ('CAI', 'LHR', 12)]:
    +link(a, b, c)
path(X, Y, C) <= link(X, Y, C)
path(X, Y, C) <= path(X, Z, K) & link(Z, Y, M) & (C == K + M)
(cheapest[X, Y] == min_(C, order_by=C)) <= path(X, Y, C)
print(sorted((cheapest[X, Y] == C).data))

# --- Python functions and text -------------------------------------
tax(X, T) <= price(X, N) & (T == vat_cents(N * 100))
root(X, T) <= price(X, N) & (T == math.sqrt(N * N))
print(sorted(tax(X, T).data), sorted(root(X, T).data))


@pyDatalog.program()
def _():
    +road('depot', 'cafe')
    near(X, Y) <= road(X, Y)


print(pyDatalog.ask("near('depot', Y)").answers)
pyDatalog.load("+road('cafe', 'school')")
print(pyDatalog.ask("road(X, 'school')").answers)
