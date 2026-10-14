from pyDatalog import pyDatalog

pyDatalog.create_terms('P, L, S, R, best, rnk, top_two')

+best('zoe', 'cave', 990)
+best('mia', 'cave', 950)
+best('leo', 'cave', 870)
+best('sam', 'cave', 700)

(rnk[P, L] == rank_(group_by=L, order_by=-S)) <= best(P, L, S)

# the slip: ranks 0, 1 and 2 are all <= 2, so three players pass
top_two(P, L) <= (rnk[P, L] == R) & (R <= 2)
print(sorted(top_two(P, 'cave').data))
