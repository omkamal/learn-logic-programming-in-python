# timeout: 200
# Bigger boards, first answer only. Each solver gets 20 s per board.
import multiprocessing as mp
import time
import clingo
from z3 import Ints, Solver, Distinct, Abs, And, sat

def z3_abs(n):                         # diagonals stated with Abs
    c = Ints(" ".join(f"c{i}" for i in range(n)))
    s = Solver()
    s.add([And(0 <= x, x < n) for x in c])
    s.add(Distinct(c))
    for i in range(n):
        for j in range(i + 1, n):
            s.add(Abs(c[i] - c[j]) != j - i)
    assert s.check() == sat

def z3_diag(n):                        # diagonals stated with Distinct
    c = Ints(" ".join(f"c{i}" for i in range(n)))
    s = Solver()
    s.add([And(0 <= x, x < n) for x in c])
    s.add(Distinct(c))
    s.add(Distinct([c[i] + i for i in range(n)]))
    s.add(Distinct([c[i] - i for i in range(n)]))
    assert s.check() == sat

def clingo_first(n):
    prog = (f"n(0..{n-1}).\n1 {{ queen(R, C) : n(C) }} 1 :- n(R).\n"
            ":- queen(R1, C), queen(R2, C), R1 < R2.\n"
            ":- queen(R1, C1), queen(R2, C2), R1 < R2,"
            " |C1 - C2| == R2 - R1.\n")
    ctl = clingo.Control(["1", "--warn=none"])   # "1": stop at the first
    ctl.add("base", [], prog)
    ctl.ground([("base", [])])
    ctl.solve()

def timed(fn, n, limit=20):
    p = mp.Process(target=fn, args=(n,))
    t = time.perf_counter()
    p.start()
    p.join(limit)
    if p.is_alive():
        p.kill()
        return f"> {limit} s"
    return f"{time.perf_counter() - t:5.2f} s"

if __name__ == "__main__":
    print("N      Z3 (Abs)   Z3 (Distinct)   clingo")
    for n in (8, 16, 24, 32, 48, 100):
        print(f"{n:<4d} {timed(z3_abs, n):>9s}  {timed(z3_diag, n):>13s}"
              f"  {timed(clingo_first, n):>8s}")
