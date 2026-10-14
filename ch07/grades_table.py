from pprint import pprint
from pyDatalog import pyDatalog

pyDatalog.create_terms('S, N, G, LO, HI, score, band, grade')

for who, pts in [('ann', 95), ('bob', 82), ('cid', 71), ('dee', 90),
                 ('eli', 55), ('fay', 88)]:
    +score(who, pts)

for letter, lo, hi in [('A', 90, 100), ('B', 80, 89), ('C', 70, 79),
                       ('F', 0, 69)]:
    +band(letter, lo, hi)

grade(S, G) <= score(S, N) & band(G, LO, HI) & (N >= LO) & (N <= HI)
pprint(sorted(grade(S, G).data), width=70, compact=True)

# the school lowers the A cut-off to 88: only facts change
-band('A', 90, 100)
-band('B', 80, 89)
+band('A', 88, 100)
+band('B', 80, 87)
pprint(sorted(grade(S, G).data), width=70, compact=True)
