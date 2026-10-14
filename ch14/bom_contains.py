from pyDatalog import pyDatalog

pyDatalog.create_terms('A, P, Q, N, has, contains')

for assembly, piece, how_many in [
        ('bicycle', 'frame', 1), ('bicycle', 'wheel', 2),
        ('bicycle', 'handlebar', 1),
        ('wheel', 'rim', 1), ('wheel', 'tire', 1), ('wheel', 'hub', 1),
        ('wheel', 'spoke', 32),
        ('hub', 'axle', 1), ('hub', 'bearing', 2),
        ('frame', 'tube', 3), ('frame', 'bolt', 4),
        ('handlebar', 'grip', 2), ('handlebar', 'bolt', 4)]:
    +has(assembly, piece, how_many)

# A contains P: P is a direct part of A, or a part of a part (and so on)
contains(A, P) <= has(A, P, N)
contains(A, P) <= contains(A, Q) & has(Q, P, N)

def names(query):
    return sorted(row[0] for row in query.data)

print('a wheel contains: ', *names(contains('wheel', P)))
print('a bicycle contains', len(names(contains('bicycle', P))),
      'different parts')
print('bolts end up in:  ', *names(contains(A, 'bolt')))
print('axles end up in:  ', *names(contains(A, 'axle')))
