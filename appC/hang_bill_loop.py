# timeout: 8
from pyDatalog import pyDatalog

pyDatalog.create_terms('A, P, Q, N, M, K, R, S, has, route, total')
for a, p, n in [('bike', 'wheel', 2), ('wheel', 'spoke', 32)]:
    +has(a, p, n)

route(A, P, S, N) <= has(A, P, N) & (S == A + '>' + P)
route(A, P, S, N) <= (route(A, Q, R, M) & has(Q, P, K)
                      & (N == M * K) & (S == R + '>' + P))
(total[A, P] == sum_(N, for_each=S)) <= route(A, P, S, N)

+has('wheel', 'bike', 1)           # a wheel that contains the bike
print('asking')
print((total['bike', 'spoke'] == N).data)
