from pyDatalog import pyDatalog

pyDatalog.create_terms('A, P, N, has')

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

print('a wheel is built from:', sorted(has('wheel', P, N).data))
print('a bicycle is built from:', sorted(has('bicycle', P, N).data))
print('bolts are used in:', sorted(has(A, 'bolt', N).data))
