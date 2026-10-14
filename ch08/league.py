from pyDatalog import pyDatalog

pyDatalog.create_terms('G, T, P, Z, W, game, points, leader, avg_pts,'
                       ' above')

# (game, team, points): 3 for a win, 1 for a draw, 0 for a loss
for g, team, pts in [(1, 'Lions', 3), (1, 'Hawks', 0),
                     (2, 'Lions', 1), (2, 'Otters', 1),
                     (3, 'Hawks', 3), (3, 'Otters', 0),
                     (4, 'Lions', 3), (4, 'Foxes', 0),
                     (5, 'Foxes', 3), (5, 'Hawks', 0),
                     (6, 'Otters', 1), (6, 'Foxes', 1)]:
    +game(g, team, pts)

(points[T] == sum_(P, for_each=G)) <= game(G, T, P)

print(sorted((points[T] == Z).data))

# an aggregate over the finished aggregate: one basket for the league
(leader['league']  == max_(T, order_by=Z))  <= (points[T] == Z)
(avg_pts['league'] == mean_(Z, for_each=T)) <= (points[T] == Z)
print(sorted((leader['league'] == W).data))
print(sorted((avg_pts['league'] == W).data))

above(T) <= (points[T] == Z) & (avg_pts['league'] == W) & (Z > W)
print(sorted(above(T).data))
