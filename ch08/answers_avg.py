from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, avg, dept, no_staff')
for name, d, pay in [('ann', 'eng', 120), ('bob', 'eng', 100),
                     ('cid', 'ops', 80), ('dee', 'ops', 90),
                     ('eli', 'hr', 70)]:
    +emp(name, d, pay)
for d in ['eng', 'ops', 'hr', 'sales']:
    +dept(d)

(avg[Y] == mean_(N, for_each=X)) <= emp(X, Y, N)
print(sorted((avg[Y] == Z).data))

no_staff(Y) <= dept(Y) & ~emp(X, Y, N)
print(sorted(no_staff(Y).data))
