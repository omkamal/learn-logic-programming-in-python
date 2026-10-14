# timeout: 8
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, one, two, reach1, reach2')
+one('A', 'A')                                   # a loop of one
for a, b in [('A', 'B'), ('B', 'A')]:            # a loop of two
    +two(a, b)

reach1(X, Y) <= one(X, Y)
reach1(X, Y) <= one(X, Z) & reach1(Z, Y)         # recursive literal last
reach2(X, Y) <= two(X, Y)
reach2(X, Y) <= two(X, Z) & reach2(Z, Y)         # recursive literal last
print(sorted(reach1('A', Y).data))
print(sorted(reach2('A', Y).data))
