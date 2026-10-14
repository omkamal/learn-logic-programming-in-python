from pyDatalog import pyDatalog

pyDatalog.create_terms('A, P, Q, N, M, K, has, uses, naive')

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

# following one chain of assemblies, N copies of P are needed
uses(A, P, N) <= has(A, P, N)
uses(A, P, N) <= uses(A, Q, M) & has(Q, P, K) & (N == M * K)

print('spokes:', sorted(uses('bicycle', 'spoke', N).data))
print('bolts: ', sorted(uses('bicycle', 'bolt', N).data))

# add the chain totals up, one per distinct number
(naive[P] == sum_(N, for_each=N)) <= uses('bicycle', P, N)
print('naive spokes:', (naive['spoke'] == N).data)
print('naive bolts: ', (naive['bolt'] == N).data)
