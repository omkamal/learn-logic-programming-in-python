from decimal import Decimal
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, Z, pay, total, richer')

staff = [('ann', 'eng', '1200.10'), ('bob', 'eng', '1000.20'),
         ('cid', 'ops', '800.35')]
for name, dept, text in staff:
    +pay(name, dept, Decimal(text))

(total[Y] == sum_(N, for_each=X)) <= pay(X, Y, N)
print(sorted((total[Y] == Z).data))

richer(X) <= pay(X, Y, N) & (N > 1000)
print(sorted(richer(X).data))
