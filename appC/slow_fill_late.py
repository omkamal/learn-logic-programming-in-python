# timeout: 60
# Six queens: check each queen right after her column, or check at the end.
import time
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, col, ok')
N = 6
for c in range(N):
    +col(c)
ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)


def board(early):
    q = pyDatalog.variables(N)
    fills = [col(v) for v in q]
    checks = [[ok(q[i], q[j], j - i) for i in range(j)] for j in range(N)]
    if early:
        parts = []
        for j in range(N):
            parts.append(fills[j])
            parts.extend(checks[j])
    else:
        parts = fills + [c for row in checks for c in row]
    body = parts[0]
    for p in parts[1:]:
        body = body & p
    t = time.perf_counter()
    n = len(body.data)
    return n, time.perf_counter() - t


n1, t_early = board(True)
n2, t_late = board(False)
print(n1, n2, 'boards, the same either way')
print('all fills first is more than 20 times slower:',
      t_late > 20 * t_early)
