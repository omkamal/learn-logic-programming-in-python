# Answer to exercise 6: routes of exactly 9 and 10 flights from CAI to JFK.
from z3 import And, Int, Or, Solver, sat

names = ["CAI", "DXB", "LHR", "JFK"]
FLIGHTS = [(0, 1), (1, 2), (2, 0), (2, 3)]

for k in (9, 10):
    stop = [Int(f"stop{i}") for i in range(k + 1)]
    s = Solver()
    s.add(stop[0] == 0, stop[k] == 3)
    for a, b in zip(stop, stop[1:]):
        s.add(Or([And(a == f, b == t) for f, t in FLIGHTS]))
    if s.check() == sat:
        m = s.model()
        print(k, " ".join(names[m[c].as_long()] for c in stop))
    else:
        print(k, None)
