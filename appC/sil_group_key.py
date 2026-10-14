from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, C, link, path, cheapest, pooled')
for a, b, c in [('CAI', 'DXB', 4), ('DXB', 'LHR', 7), ('CAI', 'LHR', 12)]:
    +link(a, b, c)

path(X, Y, C) <= link(X, Y, C)
(cheapest[X, Y] == min_(C, order_by=C)) <= path(X, Y, C)
(pooled[X] == min_(C, order_by=C)) <= path(X, Y, C)     # key too short

print(sorted((cheapest[X, Y] == C).data))
print(sorted((pooled[X] == C).data))
