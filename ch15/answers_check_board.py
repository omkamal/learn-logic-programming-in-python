from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, ok')
ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)

board = (2, 0, 3, 1)
for lower in range(1, 4):
    for upper in range(lower):
        args = (board[upper], board[lower], lower - upper)
        print('ok', args, bool(ok(*args)))
