from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, ancestor')
for a, b in [('alice', 'bob'), ('bob', 'carol')]:
    +parent(a, b)

# only the recursive clause: there is no base clause
ancestor(X, Y) <= ancestor(X, Z) & parent(Z, Y)
print(sorted(ancestor('alice', Y).data))
print(bool(ancestor('alice', 'carol')))
