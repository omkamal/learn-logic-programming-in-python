from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, best, steady')

# three people in eng earn the same top pay
for name, dept, pay in [('ann', 'eng', 120), ('bob', 'eng', 120),
                        ('abe', 'eng', 120), ('zed', 'eng', 100),
                        ('cid', 'ops', 80), ('dee', 'ops', 90)]:
    +emp(name, dept, pay)

(best[Y]   == max_(X, order_by=N))      <= emp(X, Y, N)
(steady[Y] == max_(X, order_by=(N, X))) <= emp(X, Y, N)

print(sorted((best[Y] == Z).data))      # one of the three tied names
print(sorted((steady[Y] == Z).data))    # ties broken by the name
