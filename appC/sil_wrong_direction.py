from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, ancestor')
for a, b in [('alice', 'bob'), ('bob', 'carol'), ('carol', 'dave')]:
    +parent(a, b)

ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= ancestor(X, Z) & parent(Y, Z)   # parent written backwards
print(len(ancestor(X, Y).data), 'pairs')
print(('alice', 'alice') in ancestor(X, Y).data)
