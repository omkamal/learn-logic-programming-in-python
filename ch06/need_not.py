from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, city, reach')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'),
             ('LHR', 'CAI')]:
    +flight(a, b)
for c in ['CAI', 'DXB', 'LHR', 'JFK', 'NRT']:
    +city(c)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

reached = {y for (y,) in reach('CAI', Y).data}
everywhere = {c for (c,) in city(X).data}
print('reached:   ', sorted(reached))
print('all cities:', sorted(everywhere))
print('not reached (plain Python):', sorted(everywhere - reached))
