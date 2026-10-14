from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, emp, total, headcount, top, lowest, avg, names, best, ranked, running')
for name, d, s in [('ann', 'eng', 120), ('bob', 'eng', 100), ('cid', 'ops', 80),
                   ('dee', 'ops', 90), ('eli', 'hr', 70)]:
    +emp(name, d, s)

(total[Y]     == sum_(N, for_each=X))           <= emp(X, Y, N)
(headcount[Y] == len_(X))                       <= emp(X, Y, N)
(top[Y]       == max_(N, order_by=N))           <= emp(X, Y, N)
(lowest[Y]    == min_(N, order_by=N))           <= emp(X, Y, N)
(avg[Y]       == mean_(N, for_each=X))          <= emp(X, Y, N)
(names[Y]     == concat_(X, order_by=X, sep=', ')) <= emp(X, Y, N)
(best[Y]      == max_(X, order_by=N))           <= emp(X, Y, N)      # argmax: WHO earns most

for q in (total[Y] == Z, headcount[Y] == Z, top[Y] == Z, avg[Y] == Z, names[Y] == Z, best[Y] == Z):
    print(sorted(q.data))
