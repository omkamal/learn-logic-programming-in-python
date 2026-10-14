from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, ok')
ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)

print(bool(ok(3, 5, 2)))
print(bool(ok(3, 5, 1)))
