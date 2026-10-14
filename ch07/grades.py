from pprint import pprint
from pyDatalog import pyDatalog

pyDatalog.create_terms('S, N, G, score, grade, loose')

for who, pts in [('ann', 95), ('bob', 82), ('cid', 71), ('dee', 90),
                 ('eli', 55), ('fay', 88)]:
    +score(who, pts)

grade(S, 'A') <= score(S, N) & (N >= 90)
grade(S, 'B') <= score(S, N) & (N >= 80) & (N < 90)
grade(S, 'C') <= score(S, N) & (N >= 70) & (N < 80)
grade(S, 'F') <= score(S, N) & (N < 70)

pprint(sorted(grade(S, G).data), width=70, compact=True)

# what if the upper bound of B is forgotten?
loose(S, 'A') <= score(S, N) & (N >= 90)
loose(S, 'B') <= score(S, N) & (N >= 80)
pprint(sorted(loose(S, G).data), width=70, compact=True)
