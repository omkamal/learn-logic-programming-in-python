from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, company')

for name, dept, pay in [('ann', 'eng', 120), ('bob', 'eng', 100),
                        ('cid', 'ops', 80), ('dee', 'ops', 90),
                        ('eli', 'hr', 70)]:
    +emp(name, dept, pay)

# one basket for everybody: the key is a constant, not a variable
(company['all'] == sum_(N, for_each=X)) <= emp(X, Y, N)

print(company['all'] == Z)
