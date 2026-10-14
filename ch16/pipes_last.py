# timeout: 5
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, pipe, flows_to')
for a, b in [('well', 'tank'), ('tank', 'pump'), ('pump', 'well')]:
    +pipe(a, b)                     # water goes round in a circle

flows_to(X, Y) <= pipe(X, Y)
flows_to(X, Y) <= pipe(X, Z) & flows_to(Z, Y)    # recursive literal last
print(sorted(flows_to('well', Y).data))
