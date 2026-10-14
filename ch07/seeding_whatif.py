from pyDatalog import pyDatalog

pyDatalog.create_terms('S, T, A, B, seed, mirror, late')

for rank, team in [(1, 'Lions'), (2, 'Hawks'), (3, 'Otters'),
                   (4, 'Foxes'), (5, 'Wolves'), (6, 'Bears'),
                   (7, 'Herons'), (8, 'Moles')]:
    +seed(rank, team)

# without the gate every pairing appears twice, once from each side
mirror(S, A, B) <= seed(S, A) & (T == 9 - S) & seed(T, B)
print(len(mirror(S, A, B).data))

# the calculator placed before the seed literal that fills S
late(S, A, B) <= (T == 9 - S) & seed(S, A) & seed(T, B) & (S < T)
print(sorted(late(S, A, B).data))
