from pyDatalog import pyDatalog

pyDatalog.create_terms('A, P, Q, N, has, part, leaf, top, leaf_early')

for assembly, piece, how_many in [
        ('bicycle', 'frame', 1), ('bicycle', 'wheel', 2),
        ('bicycle', 'handlebar', 1),
        ('wheel', 'rim', 1), ('wheel', 'tire', 1), ('wheel', 'hub', 1),
        ('wheel', 'spoke', 32),
        ('hub', 'axle', 1), ('hub', 'bearing', 2),
        ('frame', 'tube', 3), ('frame', 'bolt', 4),
        ('handlebar', 'grip', 2), ('handlebar', 'bolt', 4)]:
    +has(assembly, piece, how_many)

# every name that appears in the bill, as an assembly or as a part
part(P) <= has(P, Q, N)
part(P) <= has(Q, P, N)

# a leaf part contains nothing; a top-level product is used by nothing
leaf(P) <= part(P) & ~has(P, Q, N)
top(P) <= part(P) & ~has(Q, P, N)

def names(query):
    return sorted(row[0] for row in query.data)

print('all parts:', len(names(part(P))))
print('leaves:   ', *names(leaf(P)))
print('top level:', *names(top(P)))

# the same test with the "not" written first
leaf_early(P) <= ~has(P, Q, N) & part(P)
print('leaves, not-first:', names(leaf_early(P)))
print('is a bolt a leaf?', bool(leaf('bolt')),
      '/', bool(leaf_early('bolt')))
