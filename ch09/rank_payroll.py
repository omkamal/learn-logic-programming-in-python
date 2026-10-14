from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, R, emp, rnk')

+emp('ann', 'eng', 120)
+emp('bob', 'eng', 100)
+emp('cid', 'ops', 80)
+emp('dee', 'ops', 90)
+emp('eli', 'hr', 70)

(rnk[X] == rank_(group_by=Y, order_by=-N)) <= emp(X, Y, N)

print(sorted((rnk[X] == R).data))
print(rnk['bob'] == R)
print(sorted((rnk[X] == 0).data))
