# not shown in the book: does the plain-Python explorer agree with the
# pyDatalog program for every N from 4 to 8?
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, col, ok, solution')

def safe(cols, k):
    return all(cols[i] != cols[k] and abs(cols[i] - cols[k]) != k - i
               for i in range(k))

def explorer(n):
    found = []
    def walk(cols):
        if len(cols) == n:
            found.append(tuple(cols))
            return
        for c in range(n):
            cols.append(c)
            if safe(cols, len(cols) - 1):
                walk(cols)
            cols.pop()
    walk([])
    return set(found)

def engine(n):
    pyDatalog.clear()
    for c in range(n):
        +col(c)
    ok(X, Y, D) <= (X != Y) & (X - Y != D) & (Y - X != D)
    Q = pyDatalog.variables(n)
    body = None
    for j in range(n):
        for lit in [col(Q[j])] + [ok(Q[i], Q[j], j - i) for i in range(j)]:
            body = lit if body is None else body & lit
    solution(*Q) <= body
    return set(solution(*Q).data)

for n in range(4, 9):
    a, b = explorer(n), engine(n)
    print(n, len(a), len(b), a == b)
