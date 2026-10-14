from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach, on_loop')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'),
             ('LHR', 'CAI')]:          # the one new flight: LHR -> CAI
    +flight(a, b)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)   # recursive literal FIRST

print(sorted(reach('CAI', Y).data))
print(sorted(reach(X, 'JFK').data))
on_loop(X) <= reach(X, X)                   # who can get back home?
print(sorted(on_loop(X).data))
