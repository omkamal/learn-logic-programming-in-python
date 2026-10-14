from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, city, reach, hasty')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'),
             ('LHR', 'CAI')]:
    +flight(a, b)
for c in ['CAI', 'DXB', 'LHR', 'JFK', 'NRT']:
    +city(c)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

hasty(Y) <= ~reach('CAI', Y) & city(Y)       # not first

print(bool(hasty('NRT')), bool(hasty('DXB')))   # asked with a value
print(sorted(hasty(Y).data))                    # asked with a blank
