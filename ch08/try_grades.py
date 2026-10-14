from pyDatalog import pyDatalog

pyDatalog.create_terms('P, X, C, N, Z, pupil, average, best')
for pid, name, cls, score in [(1, 'ann', '7a', 92), (2, 'bo', '7a', 80),
                              (3, 'cy', '7a', 71), (4, 'di', '7b', 66),
                              (5, 'ed', '7b', 88)]:
    +pupil(pid, name, cls, score)

(average[C] == mean_(N, for_each=P)) <= pupil(P, X, C, N)
(best[C]    == max_(X, order_by=N))  <= pupil(P, X, C, N)
print(sorted((average[C] == Z).data))
print(sorted((best[C] == Z).data))
