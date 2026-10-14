# Eight queens in Z3: the unknowns are eight column numbers.
import time
from z3 import Ints, Solver, Distinct, Abs, And, Or, sat

N = 8
c = Ints(" ".join(f"c{i}" for i in range(N)))   # c[i] = column in row i
s = Solver()
s.add([And(0 <= x, x < N) for x in c])          # on the board
s.add(Distinct(c))                              # one queen per column
for i in range(N):
    for j in range(i + 1, N):
        s.add(Abs(c[i] - c[j]) != j - i)        # and none on a diagonal

t = time.perf_counter()
assert s.check() == sat
first = [s.model()[x].as_long() for x in c]
print("first answer:", first, "in", round(time.perf_counter() - t, 3), "s")

t = time.perf_counter()                         # now ask for ALL of them
found = []
while s.check() == sat:
    m = s.model()
    found.append(tuple(m[x].as_long() for x in c))
    s.add(Or([x != m[x] for x in c]))           # forbid this one, ask again
print(len(found), "solutions in", round(time.perf_counter() - t, 3), "s")
print("smallest:", sorted(found)[0])
