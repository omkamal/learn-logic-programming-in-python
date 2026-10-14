# Z3 as a SOLVER on a related yes/no question:
# "is there a route from CAI to JFK of exactly k flights?"
from z3 import And, Int, Or, Solver, sat

names = ["CAI", "DXB", "LHR", "JFK"]
FLIGHTS = [(0, 1), (1, 2), (2, 0), (2, 3)]        # the same four flights

def route_of(k):
    stop = [Int(f"stop{i}") for i in range(k + 1)]   # k + 1 unknown cities
    s = Solver()
    s.add(stop[0] == 0, stop[k] == 3)                # start CAI, end JFK
    for a, b in zip(stop, stop[1:]):                 # every hop is a flight
        s.add(Or([And(a == f, b == t) for f, t in FLIGHTS]))
    if s.check() != sat:
        return None
    m = s.model()
    return [names[m[c].as_long()] for c in stop]

for k in range(1, 8):
    print(k, route_of(k))
