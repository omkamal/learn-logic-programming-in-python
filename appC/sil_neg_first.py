from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, city, reach, ok, hasty,'
                       ' hasty_nrt')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'),
             ('LHR', 'CAI')]:
    +flight(a, b)
for c in ['CAI', 'DXB', 'LHR', 'JFK', 'NRT']:
    +city(c)
reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

ok(Y) <= city(Y) & ~reach('CAI', Y)          # fill first, not after
hasty(Y) <= ~reach('CAI', Y) & city(Y)       # not first
hasty_nrt(Y) <= ~reach('NRT', Y) & city(Y)   # not first, from Tokyo

print('fill first   ', sorted(ok(Y).data))
print('not first    ', sorted(hasty(Y).data))
print('not first, T ', len(hasty_nrt(Y).data), 'of 5 cities')
print('one value    ', bool(hasty('NRT')), bool(hasty('DXB')))
