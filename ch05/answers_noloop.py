from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach, on_loop')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK')]:
    +flight(a, b)               # Monday's network: no LHR -> CAI

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)
on_loop(X) <= reach(X, X)

print(sorted(on_loop(X).data))
