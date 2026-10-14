from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach, reached_by')

n = 200
for i in range(n):
    +link(i, i + 1)
reach(X, Y) <= link(X, Y)
reach(X, Y) <= reach(X, Z) & link(Z, Y)
reached_by(Y, X) <= link(X, Y)
reached_by(Y, X) <= reached_by(Y, Z) & link(X, Z)

slow = sorted(reach(X, n).data)
fast = sorted(reached_by(n, X).data)
print(len(slow), len(fast), 'answers; identical:', slow == fast)
