# timeout: 15
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'),
             ('LHR', 'CAI')]:
    +flight(a, b)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= flight(X, Z) & reach(Z, Y)   # recursive literal LAST

print("asking: where can Cairo get to?", flush=True)
print(sorted(reach('CAI', Y).data))
