from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, avg')

# bob earns 101 instead of 100: the engineering average is not whole
for name, dept, pay in [('ann', 'eng', 120), ('bob', 'eng', 101),
                        ('cid', 'ops', 80), ('dee', 'ops', 90),
                        ('eli', 'hr', 70)]:
    +emp(name, dept, pay)

(avg[Y] == mean_(N, for_each=X)) <= emp(X, Y, N)
print(sorted((avg[Y] == Z).data))
