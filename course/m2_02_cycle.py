from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'CAI'), ('LHR', 'JFK')]:
    +flight(a, b)          # CAI -> DXB -> LHR -> CAI is a cycle

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)   # recursive literal FIRST

print(sorted(reach('CAI', Y).data))
print(sorted(reach(X, 'JFK').data))
