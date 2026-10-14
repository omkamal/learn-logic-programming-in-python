from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach, no_direct')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'),
             ('LHR', 'CAI')]:
    +flight(a, b)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

# reach fills X and Y, then ~flight checks both
no_direct(X, Y) <= reach(X, Y) & ~flight(X, Y)

print(sorted(no_direct('CAI', Y).data))
