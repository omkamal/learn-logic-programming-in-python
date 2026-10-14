from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, emp, t1, t2, t3, t4')
+emp('ann', 'eng', 120)

# four clauses, each asking an aggregate for less than it needs
cases = [
    ('sum_ without for_each ',
     lambda: (t1[Y] == sum_(N)) <= emp(X, Y, N)),
    ('max_ with for_each    ',
     lambda: (t2[Y] == max_(N, for_each=X)) <= emp(X, Y, N)),
    ('tuple_ without order  ',
     lambda: (t3[Y] == tuple_(X)) <= emp(X, Y, N)),
    ('concat_ without sep   ',
     lambda: (t4[Y] == concat_(X, order_by=X)) <= emp(X, Y, N)),
]
for label, clause in cases:
    try:
        clause()
        print(label, 'accepted')
    except Exception as err:
        print(label, type(err).__name__ + ':', str(err).splitlines()[0])
