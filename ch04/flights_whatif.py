from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach')

for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK')]:
    +flight(a, b)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

print(sorted(reach('CAI', Y).data))
+flight('JFK', 'NRT')                       # one new fact, no new rule
print(sorted(reach('CAI', Y).data))
print(bool(reach('CAI', 'NRT')))
