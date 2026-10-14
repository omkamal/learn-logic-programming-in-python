from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, city, reach, unreachable, no_direct')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK')]:
    +flight(a, b)
for c in ['CAI', 'DXB', 'LHR', 'JFK', 'NRT']:
    +city(c)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

# negation: a city that CAI cannot reach
unreachable(Y) <= city(Y) & ~reach('CAI', Y) & (Y != 'CAI')
print(sorted(unreachable(Y).data))

# reachable but NOT directly
no_direct(X, Y) <= reach(X, Y) & ~flight(X, Y)
print(sorted(no_direct('CAI', Y).data))
