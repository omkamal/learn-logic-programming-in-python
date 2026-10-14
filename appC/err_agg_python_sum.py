from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, emp, total')
+emp('ann', 'eng', 120)

try:
    (total[Y] == sum(N, for_each=X)) <= emp(X, Y, N)   # no underscore
except Exception as err:
    print(type(err).__name__ + ':', err)
