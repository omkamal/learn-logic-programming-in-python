# timeout: 120
import time
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, col, ok, solution')

def queens(n):
    pyDatalog.clear()
    for c in range(n):
        +col(c)
    ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)
    Q = pyDatalog.variables(n)
    body = col(Q[0])
    for j in range(1, n):
        body = body & col(Q[j])
        for i in range(j):
            body = body & ok(Q[i], Q[j], j - i)
    solution(*Q) <= body
    return solution(*Q).data

print(' N  ok checks  solutions  seconds')
for n in range(4, 11):
    start = time.perf_counter()
    answers = queens(n)
    seconds = time.perf_counter() - start
    checks = n * (n - 1) // 2
    print('%2d  %9d  %9d  %7.3f' % (n, checks, len(answers), seconds))
