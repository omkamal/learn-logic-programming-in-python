from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, emp, up, down, by_pay, run_up, run_dn,'
                       ' hi, hi_dn')
for name, dept, pay in [('ann', 'eng', 100), ('bob', 'eng', 120)]:
    +emp(name, dept, pay)

(up[X] == rank_(group_by=Y, order_by=X)) <= emp(X, Y, N)
(down[X] == rank_(group_by=Y, order_by=-X)) <= emp(X, Y, N)   # X is the key
(by_pay[X] == rank_(group_by=Y, order_by=-N)) <= emp(X, Y, N) # N is not
for t in (up, down, by_pay):
    print(sorted((t[X] == N).data))

# the same on the aggregated value N, which is in the head too
(run_up[X] == running_sum_(N, group_by=Y, order_by=N)) <= emp(X, Y, N)
(run_dn[X] == running_sum_(N, group_by=Y, order_by=-N)) <= emp(X, Y, N)
for t in (run_up, run_dn):
    print(sorted((t[X] == N).data))
(hi[Y] == max_(N, order_by=N)) <= emp(X, Y, N)
(hi_dn[Y] == max_(N, order_by=-N)) <= emp(X, Y, N)
for t in (hi, hi_dn):
    print(sorted((t[Y] == N).data))
