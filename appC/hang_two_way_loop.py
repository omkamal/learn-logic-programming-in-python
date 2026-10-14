# timeout: 8
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach')
for a, b in [('A', 'B'), ('B', 'C'), ('C', 'A')]:    # a loop of three
    +flight(a, b)
+flight('B', 'A')                  # ... but one flight has a flight back

reach(X, Y) <= flight(X, Y)
reach(X, Y) <= flight(X, Z) & reach(Z, Y)    # recursive literal last
print('asking')
print(sorted(reach('A', Y).data))
