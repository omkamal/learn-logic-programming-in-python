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

# one of anything is itself; a bigger count is the sum over the direct
# sub-assemblies Q of (how many Q) times (how many P inside one Q)
(count[P, P] == 1) <= part(P)
(count[A, P] == sum_(T, for_each=Q)) <= (has(A, Q, M)
                                         & (C == count[Q, P])
                                         & (T == M * C))

print('spokes in a bicycle:', (count['bicycle', 'spoke'] == N).data)
print('bolts in a bicycle: ', (count['bicycle', 'bolt'] == N).data)
print('bearings in a wheel:', (count['wheel', 'bearing'] == N).data)
print('rows in all:', len((count[A, P] == N).data))
