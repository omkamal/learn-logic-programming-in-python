# The usual first stumble with Z3's Datalog engine: no declare_var.
from z3 import BitVecSort, BitVecVal, BoolSort, Consts, Fixedpoint, Function

CITY = BitVecSort(2)
flight = Function("flight", CITY, CITY, BoolSort())
reach = Function("reach", CITY, CITY, BoolSort())
x, y = Consts("x y", CITY)

fp = Fixedpoint()
fp.register_relation(flight, reach)
# fp.declare_var(x, y)      <- the line that is missing
fp.fact(flight(BitVecVal(0, CITY), BitVecVal(1, CITY)))
fp.rule(reach(x, y), flight(x, y))
try:
    print(fp.query(reach(BitVecVal(0, CITY), BitVecVal(1, CITY))))
except Exception as e:                       # show just the first line
    print(type(e).__name__ + ":", e.args[0].decode().splitlines()[0])
