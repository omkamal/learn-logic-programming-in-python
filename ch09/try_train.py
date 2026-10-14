from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, C, C1, C2, P, P1')
pyDatalog.create_terms('ticket, trip, cheapest, way')

+ticket('leeds', 'york', 12)
+ticket('york', 'hull', 9)
+ticket('leeds', 'hull', 30)
+ticket('hull', 'goole', 5)
+ticket('york', 'goole', 20)

trip(X, Y, C, P) <= ticket(X, Y, C) & (P == X + '>' + Y)
trip(X, Y, C, P) <= (trip(X, Z, C1, P1) & ticket(Z, Y, C2) &
                     (C == C1 + C2) & (P == P1 + '>' + Y))

(cheapest[X, Y] == min_(C, order_by=C)) <= trip(X, Y, C, P)
(way[X, Y] == min_(P, order_by=C)) <= trip(X, Y, C, P)

for goal in ('hull', 'goole'):
    print(goal, (cheapest['leeds', goal] == C).data,
          (way['leeds', goal] == P).data)
