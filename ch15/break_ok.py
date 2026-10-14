# timeout: 90
import time
from functools import reduce
from operator import and_
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, col, ok, solution')

def boards(rule):
    """Eight queens, with ok(X, Y, D) defined by `rule`."""
    pyDatalog.clear()
    for c in range(8):
        +col(c)
    ok(X, Y, D) <= rule
    Q = pyDatalog.variables(8)
    body = []
    for j in range(8):
        body.append(col(Q[j]))
        for i in range(j):
            body.append(ok(Q[i], Q[j], j - i))
    solution(*Q) <= reduce(and_, body)
    start = time.perf_counter()
    count = len(solution(*Q).data)
    return count, round(time.perf_counter() - start, 1)

full = (X != Y) & (X - Y != D) & (Y - X != D)
no_diagonals = (X != Y)
one_diagonal = (X != Y) & (X - Y != D)

print('the full rule:         %6d boards in %4.1f s' % boards(full))
print('columns only:          %6d boards in %4.1f s' % boards(no_diagonals))
print('one diagonal missing:  %6d boards in %4.1f s' % boards(one_diagonal))
