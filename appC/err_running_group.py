from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, emp, running')
+emp('ann', 'eng', 120)
+emp('bob', 'eng', 100)

try:
    # no group_by: running_sum_ refuses to start
    (running[X] == running_sum_(N, order_by=X)) <= emp(X, Y, N)
except Exception as err:
    print(type(err).__name__ + ':', err)
