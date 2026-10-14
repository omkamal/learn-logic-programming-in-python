from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach_first, reach_last')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK')]:
    +flight(a, b)               # a straight line: no flight comes back

reach_first(X, Y) <= flight(X, Y)
reach_first(X, Y) <= reach_first(X, Z) & flight(Z, Y)   # recursive FIRST

reach_last(X, Y) <= flight(X, Y)
reach_last(X, Y) <= flight(X, Z) & reach_last(Z, Y)     # recursive LAST

print('FIRST:', sorted(reach_first('CAI', Y).data))
print('LAST: ', sorted(reach_last('CAI', Y).data))
