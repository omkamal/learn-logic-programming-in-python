from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, R, S, emp, rnk, running')
for name, d, s in [('ann', 'eng', 120), ('bob', 'eng', 100), ('cid', 'ops', 80),
                   ('dee', 'ops', 90), ('eli', 'hr', 70)]:
    +emp(name, d, s)

# rank inside each department, highest salary first
(rnk[X] == rank_(group_by=Y, order_by=-N)) <= emp(X, Y, N)
print(sorted(rnk[X] == R))

# running total of salaries, in name order
(running[X] == running_sum_(N, group_by=Y, order_by=X)) <= emp(X, Y, N)
print(sorted(running[X] == S))
