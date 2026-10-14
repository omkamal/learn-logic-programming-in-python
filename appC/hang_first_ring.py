# timeout: 8
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach')
for a, b in [('A', 'B'), ('B', 'C'), ('C', 'A')]:    # a loop of three
    +flight(a, b)

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= reach(X, Z) & flight(Z, Y)    # recursive literal first
print('asking')
print(sorted(reach('A', Y).data))
