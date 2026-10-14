from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, total, big, too_soon')

for name, dept, pay in [('ann', 'eng', 120), ('bob', 'eng', 100),
                        ('cid', 'ops', 80), ('dee', 'ops', 90),
                        ('eli', 'hr', 70)]:
    +emp(name, dept, pay)

(total[Y] == sum_(N, for_each=X)) <= emp(X, Y, N)

big(Y) <= (total[Y] == Z) & (Z > 150)        # fill Z, then check it
print(sorted(big(Y).data))

too_soon(Y) <= (Z > 150) & (total[Y] == Z)   # check Z before it is filled
try:
    print(sorted(too_soon(Y).data))
except Exception as err:
    print(type(err).__name__ + ':', str(err).splitlines()[0])
