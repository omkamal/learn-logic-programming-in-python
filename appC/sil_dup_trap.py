from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, by_person, by_amount')
for name, dept, pay in [('ann', 'eng', 120), ('bob', 'eng', 120),
                        ('cid', 'ops', 80)]:
    +emp(name, dept, pay)

(by_person[Y] == sum_(N, for_each=X)) <= emp(X, Y, N)
(by_amount[Y] == sum_(N, for_each=N)) <= emp(X, Y, N)

print(sorted((by_person[Y] == Z).data))
print(sorted((by_amount[Y] == Z).data))
