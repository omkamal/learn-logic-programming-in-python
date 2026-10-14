from pyDatalog import pyDatalog

pyDatalog.create_terms('A, P, Q, N, M, K, has, uses, total')
for a, p, n in [('bike', 'frame', 1), ('bike', 'handlebar', 1),
                ('frame', 'bolt', 4), ('handlebar', 'bolt', 4)]:
    +has(a, p, n)

uses(A, P, N) <= has(A, P, N)
uses(A, P, N) <= uses(A, Q, M) & has(Q, P, K) & (N == M * K)
(total[A, P] == sum_(N, for_each=N)) <= uses(A, P, N)

print(sorted(uses('bike', 'bolt', N).data))     # two chains, one card
print((total['bike', 'bolt'] == N).data)       # 8 bolts are needed
