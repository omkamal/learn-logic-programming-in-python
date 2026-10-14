# Eight queens in clingo (answer set programming), through its Python API.
import time
import clingo

PROGRAM = """
n(0..7).
1 { queen(R, C) : n(C) } 1 :- n(R).
:- queen(R1, C), queen(R2, C), R1 < R2.
:- queen(R1, C1), queen(R2, C2), R1 < R2, |C1 - C2| == R2 - R1.
#show queen/2.
"""

ctl = clingo.Control(["0", "--warn=none"])   # "0": give me every answer set
ctl.add("base", [], PROGRAM)
t = time.perf_counter()
ctl.ground([("base", [])])
found = []

def on_model(m):
    cols = {a.arguments[0].number: a.arguments[1].number
            for a in m.symbols(shown=True)}
    found.append(tuple(cols[r] for r in range(8)))

ctl.solve(on_model=on_model)
print(len(found), "solutions in", round(time.perf_counter() - t, 3), "s")
print("smallest:", sorted(found)[0])
