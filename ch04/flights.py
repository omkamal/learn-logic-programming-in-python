from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach')

for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK')]:
    +flight(a, b)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

print(sorted(reach('CAI', Y).data))     # where can Cairo reach?
print(sorted(reach(X, 'JFK').data))     # who can reach New York?
print(bool(reach('CAI', 'JFK')))        # yes or no
print(bool(reach('CAI', 'NRT')))        # Tokyo has no flights
