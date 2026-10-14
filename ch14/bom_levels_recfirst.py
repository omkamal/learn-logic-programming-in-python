# timeout: 10
from pyDatalog import pyDatalog

pyDatalog.create_terms('A, P, Q, N, M, C, T, has, part, count')

# has(assembly, part, how many go into ONE assembly)
for assembly, piece, how_many in [
        ('bicycle', 'frame', 1), ('bicycle', 'wheel', 2),
        ('bicycle', 'handlebar', 1),
        ('wheel', 'rim', 1), ('wheel', 'tire', 1), ('wheel', 'hub', 1),
        ('wheel', 'spoke', 32),
        ('hub', 'axle', 1), ('hub', 'bearing', 2),
        ('frame', 'tube', 3), ('frame', 'bolt', 4),
        ('handlebar', 'grip', 2), ('handlebar', 'bolt', 4)]:
    +has(assembly, piece, how_many)

part(P) <= has(P, Q, N)
part(P) <= has(Q, P, N)

(count[P, P] == 1) <= part(P)
# the recursive literal first, as in a reach rule
(count[A, P] == sum_(T, for_each=Q)) <= ((C == count[Q, P])
                                         & has(A, Q, M)
                                         & (T == M * C))

print('spokes in a bicycle:', (count['bicycle', 'spoke'] == N).data)
