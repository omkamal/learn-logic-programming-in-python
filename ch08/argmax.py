from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, top, best')

for name, dept, pay in [('ann', 'eng', 120), ('bob', 'eng', 100),
                        ('cid', 'ops', 80), ('dee', 'ops', 90),
                        ('eli', 'hr', 70)]:
    +emp(name, dept, pay)

(top[Y]  == max_(N, order_by=N)) <= emp(X, Y, N)    # the highest pay
(best[Y] == max_(X, order_by=N)) <= emp(X, Y, N)    # who earns it: argmax

print(sorted((top[Y] == Z).data))
print(sorted((best[Y] == Z).data))
