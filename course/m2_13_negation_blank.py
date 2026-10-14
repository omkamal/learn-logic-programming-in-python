from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, city, reach, cai_misses, nrt_misses')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK')]:
    +flight(a, b)
for c in ['CAI', 'DXB', 'LHR', 'JFK', 'NRT']:
    +city(c)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

cai_misses(Y) <= ~reach('CAI', Y) & city(Y)   # the negation comes first: Y is blank
nrt_misses(Y) <= ~reach('NRT', Y) & city(Y)   # same shape, Tokyo reaches nobody

print(sorted(cai_misses(Y).data))
print(sorted(nrt_misses(Y).data))
