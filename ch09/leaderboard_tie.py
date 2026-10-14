from pyDatalog import pyDatalog

pyDatalog.create_terms('P, L, S, R, best, rnk')

+best('leo', 'forest', 880)
+best('kai', 'forest', 880)
+best('zoe', 'forest', 640)
+best('mia', 'forest', 620)

(rnk[P, L] == rank_(group_by=L, order_by=-S)) <= best(P, L, S)

print(sorted((rnk[P, 'forest'] == R).data, key=lambda row: row[1]))
