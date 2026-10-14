from pprint import pprint
from pyDatalog import pyDatalog

pyDatalog.create_terms('S, T, A, B, seed, match')

for rank, team in [(1, 'Lions'), (2, 'Hawks'), (3, 'Otters'),
                   (4, 'Foxes'), (5, 'Wolves'), (6, 'Bears'),
                   (7, 'Herons'), (8, 'Moles')]:
    +seed(rank, team)

# seed S meets seed 9 - S; the gate S < T keeps one copy of each pairing
match(S, A, B) <= seed(S, A) & (T == 9 - S) & seed(T, B) & (S < T)
pprint(sorted(match(S, A, B).data), width=70, compact=True)
