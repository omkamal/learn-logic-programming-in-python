from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, C, C1, C2, P, P1, link, route, best')

+link('CAI', 'DXB', 4)
+link('DXB', 'LHR', 7)
+link('CAI', 'LHR', 12)
+link('LHR', 'JFK', 8)
+link('DXB', 'JFK', 14)

route(X, Y, C, P) <= link(X, Y, C) & (P == X + '>' + Y)
route(X, Y, C, P) <= (route(X, Z, C1, P1) & link(Z, Y, C2) &
                      (C == C1 + C2) & (P == P1 + '>' + Y))

(best[X, Y] == min_(P, order_by=C)) <= route(X, Y, C, P)

for row in sorted(route('CAI', 'JFK', C, P).data):
    print(row)
print(best['CAI', 'JFK'] == P)
print(sorted((best['CAI', Y] == P).data))
