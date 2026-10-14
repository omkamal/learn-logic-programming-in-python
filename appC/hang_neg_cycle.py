# timeout: 8
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, city, a, b')
for c in ['CAI', 'DXB']:
    +city(c)

a(X) <= city(X) & ~b(X)            # each rule is the not of the other
b(X) <= city(X) & ~a(X)
print('asking')
print(sorted(a(X).data))
