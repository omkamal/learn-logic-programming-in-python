# 4 queens as a Z3 problem: the unknowns are four column numbers.
from z3 import Ints, Solver, Distinct, Abs, And, Or, sat

c = Ints("c1 c2 c3 c4")           # c[i] = column of the queen in row i+1
s = Solver()
s.add([And(1 <= x, x <= 4) for x in c])  # every queen is on the board
s.add(Distinct(c))                       # no two in the same column
for i in range(4):
    for j in range(i + 1, 4):            # no two on the same diagonal
        s.add(Abs(c[i] - c[j]) != j - i)

while s.check() == sat:                  # as long as a placement exists
    m = s.model()
    print([m[x].as_long() for x in c])
    s.add(Or([x != m[x] for x in c]))    # forbid this answer, look again
print("no more placements")
