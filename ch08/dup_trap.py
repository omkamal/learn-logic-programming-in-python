from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, Z, emp, total, wrong, heads, wrong_heads')

# bob gets a raise: now he earns 120, exactly like ann
for name, dept, pay in [('ann', 'eng', 120), ('bob', 'eng', 120),
                        ('cid', 'ops', 80), ('dee', 'ops', 90),
                        ('eli', 'hr', 70)]:
    +emp(name, dept, pay)

(total[Y] == sum_(N, for_each=X)) <= emp(X, Y, N)   # one pay per person
(wrong[Y] == sum_(N, for_each=N)) <= emp(X, Y, N)   # one pay per amount
print(sorted((total[Y] == Z).data))
print(sorted((wrong[Y] == Z).data))

(heads[Y] == len_(X)) <= emp(X, Y, N)               # count the people
(wrong_heads[Y] == len_(N)) <= emp(X, Y, N)         # count the amounts
print(sorted((heads[Y] == Z).data))
print(sorted((wrong_heads[Y] == Z).data))
