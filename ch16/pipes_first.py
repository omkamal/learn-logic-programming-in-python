from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, pipe, flows_to')
for a, b in [('well', 'tank'), ('tank', 'pump'), ('pump', 'well')]:
    +pipe(a, b)                     # water goes round in a circle

flows_to(X, Y) <= pipe(X, Y)
flows_to(X, Y) <= flows_to(X, Z) & pipe(Z, Y)    # recursive literal first
print(sorted(flows_to('well', Y).data))
