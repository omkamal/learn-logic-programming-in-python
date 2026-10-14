from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, t1, t2, t3, t4, t5, t6, t7')
+emp('ann', 'eng', 120)

cases = [
    ('python sum', lambda: ((t1[Y] == sum(N, for_each=X))
                            <= emp(X, Y, N))),
    ('sum_ alone', lambda: ((t2[Y] == sum_(N))
                            <= emp(X, Y, N))),
    ('max_ for_each', lambda: ((t3[Y] == max_(N, for_each=X))
                               <= emp(X, Y, N))),
    ('mean_ alone', lambda: ((t4[Y] == mean_(N))
                             <= emp(X, Y, N))),
    ('concat_ no sep', lambda: ((t5[Y] == concat_(X, order_by=X))
                                <= emp(X, Y, N))),
    ('tuple_ alone', lambda: ((t6[Y] == tuple_(X))
                              <= emp(X, Y, N))),
    ('in the body', lambda: (t7(Y) <= (Z == sum_(N, for_each=X))
                             & emp(X, Y, N))),
]

for label, make_clause in cases:
    try:
        make_clause()
        print(label + ': accepted')
    except Exception as err:
        print(label + ':', type(err).__name__ + ':',
              str(err).splitlines()[0])
