from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, parent, ancestor')

+parent('alice', 'bob')
+parent('bob', 'carol')
+parent('carol', 'dave')

ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= ancestor(X, Z) & parent(Z, Y)

print(bool(ancestor('alice', 'dave')))    # is alice above dave?
print(bool(ancestor('dave', 'alice')))    # is dave above alice?
print(ancestor('dave', Y))                # who is below dave?
print(len(ancestor(X, Y).data))           # how many pairs in all?
