from pyDatalog import pyDatalog

pyDatalog.create_terms('P, B, R, K, read, rnk, place')

+read('ivy', 14)
+read('ned', 9)
+read('uma', 14)
+read('vic', 3)
+read('wes', 9)

(rnk[P] == rank_(order_by=(-B, P))) <= read(P, B)
(place[P] == K) <= (rnk[P] == R) & (K == R + 1)
for row in sorted((place[P] == K).data, key=lambda row: row[1]):
    print(row)
