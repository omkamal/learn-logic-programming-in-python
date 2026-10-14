from pyDatalog import pyDatalog

pyDatalog.create_terms('A, P, Q, N, M, K, R, S, has, contains, bad_part')
pyDatalog.create_terms('route')

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

contains(A, P) <= has(A, P, N)
contains(A, P) <= contains(A, Q) & has(Q, P, N)
bad_part(P) <= contains(P, P)

print('before the slip:', sorted(bad_part(P).data))
+has('wheel', 'bicycle', 1)       # a slip: the wheel "contains" a bicycle
print('after the slip: ', sorted(bad_part(P).data))
