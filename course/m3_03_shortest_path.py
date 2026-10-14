from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, C, C1, C2, link, path, cheapest')
for a, b, c in [('CAI', 'DXB', 4), ('DXB', 'LHR', 7), ('CAI', 'LHR', 12), ('LHR', 'JFK', 8), ('DXB', 'JFK', 14)]:
    +link(a, b, c)

path(X, Y, C) <= link(X, Y, C)
path(X, Y, C) <= path(X, Z, C1) & link(Z, Y, C2) & (C == C1 + C2)
(cheapest[X, Y] == min_(C, order_by=C)) <= path(X, Y, C)

print(sorted(path('CAI', 'JFK', C).data))
print(cheapest['CAI', 'JFK'] == C)
