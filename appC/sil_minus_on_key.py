from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N, emp, up, down, by_pay')
for name, dept, pay in [('ann', 'eng', 100), ('bob', 'eng', 120)]:
    +emp(name, dept, pay)

(up[X] == rank_(group_by=Y, order_by=X)) <= emp(X, Y, N)
(down[X] == rank_(group_by=Y, order_by=-X)) <= emp(X, Y, N)   # X is the key
(by_pay[X] == rank_(group_by=Y, order_by=-N)) <= emp(X, Y, N) # N is not
for t in (up, down, by_pay):
    print(sorted((t[X] == N).data))
