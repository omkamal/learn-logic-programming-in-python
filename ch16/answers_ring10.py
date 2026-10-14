from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach')
for i in range(10):
    +link(i, (i + 1) % 10)
reach(X, Y) <= link(X, Y)
reach(X, Y) <= reach(X, Z) & link(Z, Y)
print(len(reach(X, Y).data), 'pairs on a ring of 10 stops')
