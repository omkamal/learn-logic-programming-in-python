from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, ok')

ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)

# ok only CHECKS: it cannot fill in a blank column for us
try:
    print(ok(1, Y, 1))
except Exception as error:
    print(type(error).__name__ + ':', error)
