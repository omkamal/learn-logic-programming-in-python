from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, col, ok, pair, Q0, Q1')

for c in range(4):
    +col(c)

ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)

# wrong: the check comes BEFORE the second queen has a column
pair(Q0, Q1) <= col(Q0) & ok(Q0, Q1, 1) & col(Q1)

try:
    print(pair(Q0, Q1).data)
except Exception as error:
    print(type(error).__name__ + ':', error)
