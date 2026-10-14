from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, Z, emp, by_person, by_amount')
# cid gets a raise to 90, the same as dee
for name, dept, pay in [('ann', 'eng', 120), ('bob', 'eng', 100),
                        ('cid', 'ops', 90), ('dee', 'ops', 90),
                        ('eli', 'hr', 70)]:
    +emp(name, dept, pay)

(by_person[Y] == sum_(N, for_each=X)) <= emp(X, Y, N)
(by_amount[Y] == sum_(N, for_each=N)) <= emp(X, Y, N)
print(sorted((by_person[Y] == Z).data))
print(sorted((by_amount[Y] == Z).data))
