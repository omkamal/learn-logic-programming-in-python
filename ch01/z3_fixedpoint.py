# Z3's built-in Datalog engine (Fixedpoint) on the flights, loop included.
from z3 import (BitVecSort, BitVecVal, BoolSort, Consts, Fixedpoint,
                Function, sat)

CITY = BitVecSort(2)                          # four cities fit in two bits
names = ["CAI", "DXB", "LHR", "JFK"]
code = {n: BitVecVal(i, CITY) for i, n in enumerate(names)}

flight = Function("flight", CITY, CITY, BoolSort())
reach = Function("reach", CITY, CITY, BoolSort())
x, y, z = Consts("x y z", CITY)

fp = Fixedpoint()
fp.set(engine="datalog")                      # the bottom-up Datalog engine
fp.register_relation(flight, reach)
fp.declare_var(x, y, z)                       # needed: else "Uninterpreted"

flights = [("CAI", "DXB"), ("DXB", "LHR"), ("LHR", "CAI"), ("LHR", "JFK")]
for a, b in flights:
    fp.fact(flight(code[a], code[b]))
fp.rule(reach(x, y), flight(x, y))
fp.rule(reach(x, y), [flight(x, z), reach(z, y)])

print("CAI reaches JFK:", fp.query(reach(code["CAI"], code["JFK"])) == sat)
print("JFK reaches CAI:", fp.query(reach(code["JFK"], code["CAI"])) == sat)

if fp.query(reach(code["CAI"], y)) == sat:    # a question with a blank
    answer = fp.get_answer()                  # Or(Var(0) == 1, ...)
    cities = sorted(names[c.arg(1).as_long()] for c in answer.children())
    print("CAI reaches:", cities)
