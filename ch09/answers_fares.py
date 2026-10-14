from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, C, C1, C2, P, P1')
pyDatalog.create_terms('fare, trip, cheapest, way')

+fare('A', 'B', 10)
+fare('A', 'C', 3)
+fare('C', 'B', 4)
+fare('B', 'D', 5)
+fare('C', 'D', 12)

trip(X, Y, C, P) <= fare(X, Y, C) & (P == X + '>' + Y)
trip(X, Y, C, P) <= (trip(X, Z, C1, P1) & fare(Z, Y, C2) &
                     (C == C1 + C2) & (P == P1 + '>' + Y))

(cheapest[X, Y] == min_(C, order_by=C)) <= trip(X, Y, C, P)
(way[X, Y] == min_(P, order_by=C)) <= trip(X, Y, C, P)

for row in sorted(trip('A', 'D', C, P).data):
    print(row)
print((cheapest['A', 'D'] == C).data, (way['A', 'D'] == P).data)
print((cheapest['A', 'B'] == C).data, (way['A', 'B'] == P).data)
