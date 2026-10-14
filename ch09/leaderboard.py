from pyDatalog import pyDatalog

pyDatalog.create_terms('P, L, S, R, K, best, rnk, podium, place')

+best('zoe', 'cave', 990)
+best('mia', 'cave', 950)
+best('leo', 'cave', 870)
+best('sam', 'cave', 700)
+best('leo', 'forest', 880)
+best('zoe', 'forest', 640)
+best('mia', 'forest', 620)
+best('sam', 'castle', 400)
+best('zoe', 'castle', 300)

(rnk[P, L] == rank_(group_by=L, order_by=-S)) <= best(P, L, S)
podium(P, L) <= (rnk[P, L] == R) & (R < 3)
(place[P, L] == K) <= (rnk[P, L] == R) & (K == R + 1)

print(sorted((rnk[P, 'cave'] == R).data))
print(sorted((place[P, 'forest'] == K).data))
for board in ('cave', 'forest', 'castle'):
    print(board, sorted(name for (name,) in podium(P, board).data))
