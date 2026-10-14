from pyDatalog import pyDatalog

pyDatalog.create_terms('P, X, C, N, Z, pupil, by_name, by_id, n_name, n_id')

# 7a: two different pupils are both called sam, and both scored 80
# 7b: two different pupils are both called zoe, with scores 70 and 90
for pid, name, cls, score in [(1, 'ann', '7a', 92), (2, 'sam', '7a', 80),
                              (3, 'sam', '7a', 80), (4, 'zoe', '7b', 70),
                              (5, 'zoe', '7b', 90)]:
    +pupil(pid, name, cls, score)

(by_name[C] == mean_(N, for_each=X)) <= pupil(P, X, C, N)
(by_id[C]   == mean_(N, for_each=P)) <= pupil(P, X, C, N)
print(sorted((by_name[C] == Z).data))
print(sorted((by_id[C] == Z).data))

(n_name[C] == len_(X)) <= pupil(P, X, C, N)
(n_id[C]   == len_(P)) <= pupil(P, X, C, N)
print(sorted((n_name[C] == Z).data))
print(sorted((n_id[C] == Z).data))
