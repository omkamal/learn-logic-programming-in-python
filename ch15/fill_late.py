# timeout: 120
import time
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, col, ok, solution')

def seconds_for(n, check_early):
    pyDatalog.clear()
    for c in range(n):
        +col(c)
    ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)
    Q = pyDatalog.variables(n)
    fills = [col(q) for q in Q]
    checks = [ok(Q[i], Q[j], j - i) for j in range(n) for i in range(j)]
    if check_early:                # row by row: place, then check at once
        body = []
        for j in range(n):
            body.append(fills[j])
            body += [ok(Q[i], Q[j], j - i) for i in range(j)]
    else:                          # every column first, every check after
        body = fills + checks
    clause = body[0]
    for literal in body[1:]:
        clause = clause & literal
    solution(*Q) <= clause
    start = time.perf_counter()
    count = len(solution(*Q).data)
    return count, time.perf_counter() - start

print('N  solutions  check at once  all columns first')
for n in range(4, 8):
    count, early = seconds_for(n, True)
    same, late = seconds_for(n, False)
    print('%d  %9d  %11.3f s  %14.3f s' % (n, count, early, late))
    assert count == same
