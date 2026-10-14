from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, S, emp, running, by_pay')

+emp('ann', 'eng', 120)
+emp('bob', 'eng', 100)
+emp('cid', 'ops', 80)
+emp('dee', 'ops', 90)
+emp('eli', 'hr', 70)

(running[X] == running_sum_(N, group_by=Y, order_by=X)) <= emp(X, Y, N)
print(sorted((running[X] == S).data))

# the same rows walked in a different order: smallest salary first
(by_pay[X] == running_sum_(N, group_by=Y, order_by=N)) <= emp(X, Y, N)
print(sorted((by_pay[X] == S).data))
