# timeout: 8
from pyDatalog import pyDatalog

pyDatalog.create_terms('A, P, Q, N, M, C, T, has, part, count, count2')
for a, p, n in [('bike', 'wheel', 2), ('wheel', 'spoke', 32)]:
    +has(a, p, n)
part(P) <= has(P, Q, N)
part(P) <= has(Q, P, N)
(count[P, P] == 1) <= part(P)
(count2[P, P] == 1) <= part(P)

# fill first: has() hands out Q, then count[Q, P] is asked
(count[A, P] == sum_(T, for_each=Q)) <= (has(A, Q, M)
                                         & (C == count[Q, P])
                                         & (T == M * C))
print('fill first:', (count['bike', 'spoke'] == N).data)

# the recursive literal first, as in a reach rule
(count2[A, P] == sum_(T, for_each=Q)) <= ((C == count2[Q, P])
                                          & has(A, Q, M)
                                          & (T == M * C))
print('asking the recursive-first version')
print((count2['bike', 'spoke'] == N).data)
