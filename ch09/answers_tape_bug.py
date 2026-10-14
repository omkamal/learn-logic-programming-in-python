from pyDatalog import pyDatalog

pyDatalog.create_terms('T, A, D, N, S, tx, bal, line')

+tx('t1', 'ola', 1, 200)
+tx('t2', 'ola', 2, -150)
+tx('t3', 'ola', 3, -120)

# the slip: sorted by amount instead of by day
(bal[T] == running_sum_(N, group_by=A, order_by=N)) <= tx(T, A, D, N)
line(D, N, S) <= tx(T, A, D, N) & (bal[T] == S)
for row in sorted(line(D, N, S).data):
    print(row)
