from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, Z, emp, total, wrong')
# bob gets a raise: now he earns 120, exactly like ann
for name, d, s in [('ann', 'eng', 120), ('bob', 'eng', 120), ('cid', 'ops', 80),
                   ('dee', 'ops', 90), ('eli', 'hr', 70)]:
    +emp(name, d, s)

(total[Y] == sum_(N, for_each=X)) <= emp(X, Y, N)   # one salary per person
(wrong[Y] == sum_(N, for_each=N)) <= emp(X, Y, N)   # one salary per distinct amount
print(sorted(total[Y] == Z))
print(sorted(wrong[Y] == Z))
