# timeout: 120
# One big loop (a ring of N towns), all pairs, five engines, one harness.
import os
import sqlite3
import subprocess
import tempfile
import time
import clingo
from pyDatalog import pyDatalog
from z3 import (BitVecSort, BitVecVal, BoolSort, Consts, Fixedpoint,
                Function, sat)

SWIPL = "swipl"                             # found on the PATH
edges = []                                  # filled in for each ring size

pyDatalog.create_terms("flight, reach, X, Y, Z")    # at module level


def with_pydatalog():
    pyDatalog.clear()                       # forget the previous ring
    for a, b in edges:
        +flight(a, b)
    reach(X, Y) <= flight(X, Y)
    reach(X, Y) <= reach(X, Z) & flight(Z, Y)
    return len(reach(X, Y).data)


def with_prolog():
    with tempfile.NamedTemporaryFile("w", suffix=".pl", delete=False) as f:
        f.write(":- table reach/2.\n")
        f.writelines(f"flight({a},{b}).\n" for a, b in edges)
        f.write("reach(X,Y) :- flight(X,Y).\n")
        f.write("reach(X,Y) :- flight(X,Z), reach(Z,Y).\n")
        f.write(":- aggregate_all(count, reach(_,_), C), writeln(C).\n")
    r = subprocess.run([SWIPL, "-q", "-g", "halt", f.name],
                       capture_output=True, text=True)
    os.unlink(f.name)
    return int(r.stdout.strip())


def with_sqlite():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE flight(src INT, dst INT)")
    db.executemany("INSERT INTO flight VALUES (?,?)", edges)
    q = """WITH RECURSIVE reach(src, dst) AS (
               SELECT src, dst FROM flight
             UNION
               SELECT reach.src, flight.dst
               FROM reach JOIN flight ON flight.src = reach.dst)
           SELECT count(*) FROM reach"""
    return db.execute(q).fetchone()[0]


def with_clingo():
    ctl = clingo.Control(["0", "--warn=none"])
    prog = "".join(f"flight({a},{b}).\n" for a, b in edges)
    prog += "reach(X,Y) :- flight(X,Y).\n"
    prog += "reach(X,Y) :- flight(X,Z), reach(Z,Y).\n"
    prog += "#show reach/2.\n"
    ctl.add("base", [], prog)
    ctl.ground([("base", [])])
    n = []
    ctl.solve(on_model=lambda m: n.append(len(m.symbols(shown=True))))
    return n[0]


def with_z3():
    bits = max(1, (len(edges) - 1).bit_length())
    S = BitVecSort(bits)
    flight = Function("flight", S, S, BoolSort())
    reach = Function("reach", S, S, BoolSort())
    x, y, z = Consts("x y z", S)
    fp = Fixedpoint()
    fp.set(engine="datalog")
    fp.register_relation(flight, reach)
    fp.declare_var(x, y, z)
    for a, b in edges:
        fp.fact(flight(BitVecVal(a, S), BitVecVal(b, S)))
    fp.rule(reach(x, y), flight(x, y))
    fp.rule(reach(x, y), [flight(x, z), reach(z, y)])
    assert fp.query(reach(x, y)) == sat
    return len(fp.get_answer().children())


ENGINES = [("pyDatalog", with_pydatalog),
           ("SWI-Prolog, tabled", with_prolog),
           ("SQLite CTE, UNION", with_sqlite),
           ("clingo", with_clingo),
           ("Z3 Fixedpoint", with_z3)]

for N in (100, 200, 400, 800):
    edges = [(i, (i + 1) % N) for i in range(N)]    # town i -> town i+1
    print(f"ring of {N} towns: every town reaches every town "
          f"= {N * N} pairs")
    for name, fn in ENGINES:
        t = time.perf_counter()
        count = fn()
        secs = time.perf_counter() - t
        ok = "ok" if count == N * N else "WRONG"
        print(f"  {name:20s} {count:7d} pairs {secs:6.2f} s  {ok}")
