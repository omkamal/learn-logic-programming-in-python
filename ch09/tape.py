from pyDatalog import pyDatalog

pyDatalog.create_terms('T, A, D, N, S, tx, bal, line, overdrawn, first_od')

+tx('t3', 'ola', 3, -120)
+tx('t1', 'ola', 1, 200)
+tx('t6', 'ola', 7, -90)
+tx('t2', 'ola', 2, -150)
+tx('t5', 'ola', 5, 300)
+tx('t8', 'max', 2, 100)
+tx('t7', 'max', 1, 100)
+tx('t9', 'max', 4, -50)
+tx('t10', 'ola', 9, -200)

(bal[T] == running_sum_(N, group_by=A, order_by=D)) <= tx(T, A, D, N)

line(A, D, N, S) <= tx(T, A, D, N) & (bal[T] == S)
overdrawn(A, D) <= line(A, D, N, S) & (S < 0)
(first_od[A] == min_(D, order_by=D)) <= overdrawn(A, D)

for row in sorted(line(A, D, N, S).data):
    print(row)
print(sorted(overdrawn(A, D).data))
print(sorted((first_od[A] == D).data))
