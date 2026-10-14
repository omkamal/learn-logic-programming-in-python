from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, D, col, ok, solution')

n = 6
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

print(n * (n - 1) // 2, 'ok checks')
for board in sorted(solution(*Q).data):
    print(board)
