from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, total')

for name, dept, pay in [('ann', 'eng', 120), ('bob', 'eng', 100),
                        ('cid', 'ops', 80), ('dee', 'ops', 90),
                        ('eli', 'hr', 70)]:
    +emp(name, dept, pay)

(total[Y] == sum_(N, for_each=X)) <= emp(X, Y, N)

print(sorted((total[Y] == 170).data))        # which department is 170?
print(sorted((total[Y] == Z).data))

+emp('fay', 'hr', 50)                        # a new hire: one new fact
print(sorted((total[Y] == Z).data))
