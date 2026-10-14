from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, t')
+emp('ann', 'eng', 120)

try:
    t(Y) <= (Z == sum_(N, for_each=X)) & emp(X, Y, N)   # aggregate in body
except Exception as err:
    print(type(err).__name__ + ':', err)
