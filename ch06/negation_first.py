from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, city, reach')
pyDatalog.create_terms('misses, hasty, hasty_tokyo')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'),
             ('LHR', 'CAI')]:
    +flight(a, b)
for c in ['CAI', 'DXB', 'LHR', 'JFK', 'NRT']:
    +city(c)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

misses(Y) <= city(Y) & ~reach('CAI', Y)      # fill Y first
hasty(Y) <= ~reach('CAI', Y) & city(Y)       # not first: Y still blank
hasty_tokyo(Y) <= ~reach('NRT', Y) & city(Y) # not first, from Tokyo

print(sorted(misses(Y).data))
print(sorted(hasty(Y).data))
print(sorted(hasty_tokyo(Y).data))
