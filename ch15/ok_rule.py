from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, ok')

# ok(X, Y, D): queens in columns X and Y, D rows apart, are safe
ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)

# upper queen in column 1, lower queen one row down in column ...
for args in [(1, 3, 1), (1, 1, 1), (1, 2, 1), (1, 0, 1)]:
    print('ok', args, bool(ok(*args)))

# the same two columns, but the queens are two rows apart
print('ok', (0, 2, 1), bool(ok(0, 2, 1)))
print('ok', (0, 2, 2), bool(ok(0, 2, 2)))
