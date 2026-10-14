from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, R, K, emp, rnk, place')

+emp('ann', 'eng', 120)
+emp('bob', 'eng', 100)
+emp('cid', 'ops', 80)
+emp('dee', 'ops', 90)
+emp('eli', 'hr', 70)

(rnk[X] == rank_(group_by=Y, order_by=-N)) <= emp(X, Y, N)

# a podium number that starts at 1: add one to the rank
(place[X] == K) <= (rnk[X] == R) & (K == R + 1)

print(sorted((place[X] == K).data))
