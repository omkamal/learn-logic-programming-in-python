from pyDatalog import pyDatalog

pyDatalog.create_terms('T, A, D, N, S, tx, bal')

+tx('t1', 'ola', 1, 200)
+tx('t2', 'ola', 2, -150)
+tx('t4', 'ola', 3, -20)
+tx('t3', 'ola', 3, -120)
+tx('t5', 'ola', 5, 300)

(bal[T] == running_sum_(N, group_by=A, order_by=D)) <= tx(T, A, D, N)

print(sorted((bal[T] == S).data))
