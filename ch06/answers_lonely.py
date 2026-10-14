from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, city, reach, lonely')
pyDatalog.create_terms('no_flight_in, apart, sharm')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'),
             ('LHR', 'CAI')]:
    +flight(a, b)
for c in ['CAI', 'DXB', 'LHR', 'JFK', 'NRT']:
    +city(c)
reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)

lonely(X) <= ~flight(X, Y)                   # exercise 1
print(sorted(lonely(X).data))

no_flight_in(Y) <= city(Y) & ~flight(X, Y)   # exercise 3
print(sorted(no_flight_in(Y).data))

apart(X, Y) <= city(X) & city(Y) & ~reach(X, Y)   # exercise 6
print(len(apart(X, Y).data), 'pairs')

sharm(Y) <= city(Y) & ~reach('CAI', Y)       # exercise 5
+city('SSH')                                 # a new airport, no flights yet
print(sorted(sharm(Y).data))
