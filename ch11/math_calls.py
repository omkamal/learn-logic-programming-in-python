import math
from pyDatalog import pyDatalog

before = math.sqrt.__name__
pyDatalog.create_terms('P, Q, A, B, C, D, E, spot, apart, math.sqrt')

# three spots on a flat map, in kilometers east and north of the depot
+spot('depot', 0, 0)
+spot('cafe', 3, 4)
+spot('school', 6, 8)

apart(P, Q, E) <= (spot(P, A, B) & spot(Q, C, D) & (P < Q) &
                   (E == math.sqrt((A - C) ** 2 + (B - D) ** 2)))
for row in sorted(apart(P, Q, E).data):
    print(row)

# an ordinary call still works the way it always did
print(math.sqrt(2), before, math.sqrt.__name__)
