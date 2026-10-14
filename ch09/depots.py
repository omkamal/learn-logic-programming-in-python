from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, M, M1, M2, P, P1')
pyDatalog.create_terms('road, trip, quickest, way')

+road('hub', 'north', 20)
+road('hub', 'east', 45)
+road('north', 'east', 15)
+road('north', 'mill', 50)
+road('east', 'mill', 20)
+road('east', 'port', 60)
+road('mill', 'port', 10)

trip(X, Y, M, P) <= road(X, Y, M) & (P == X + '>' + Y)
trip(X, Y, M, P) <= (trip(X, Z, M1, P1) & road(Z, Y, M2) &
                     (M == M1 + M2) & (P == P1 + '>' + Y))

(quickest[X, Y] == min_(M, order_by=M)) <= trip(X, Y, M, P)
(way[X, Y] == min_(P, order_by=M)) <= trip(X, Y, M, P)

for row in sorted(trip('hub', 'port', M, P).data):
    print(row)
print((quickest['hub', 'port'] == M).data)
print((way['hub', 'port'] == P).data)
