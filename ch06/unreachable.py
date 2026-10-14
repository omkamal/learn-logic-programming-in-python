from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, city, reach, unreachable')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'),
             ('LHR', 'CAI')]:
    +flight(a, b)
for c in ['CAI', 'DXB', 'LHR', 'JFK', 'NRT']:
    +city(c)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

unreachable(Y) <= city(Y) & ~reach('CAI', Y)   # fill Y, then say not

print(sorted(unreachable(Y).data))
print(bool(unreachable('NRT')), bool(unreachable('JFK')))
