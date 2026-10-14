from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, total, big')
for name, dept, pay in [('ann', 'eng', 120), ('bob', 'eng', 100),
                        ('cid', 'ops', 80)]:
    +emp(name, dept, pay)
(total[Y] == sum_(N, for_each=X)) <= emp(X, Y, N)

big(Y) <= (Z > 150) & (total[Y] == Z)        # gate before the table
try:
    print(big(Y))
except Exception as err:
    print(type(err).__name__ + ':', err)
