# Answer to exercise 5: the party rules plus "Cid comes only if Ann does".
from z3 import Bools, Implies, And, Or, Not, Solver, sat

ann, bob, cid = Bools("ann bob cid")
s = Solver()
s.add(Implies(ann, bob), Not(And(bob, cid)), Or(ann, bob, cid))
s.add(Implies(cid, ann))                      # the new rule

lists = []
while s.check() == sat:
    m = s.model()
    vals = {p: bool(m.eval(p, model_completion=True))
            for p in (ann, bob, cid)}
    lists.append([str(p) for p, v in vals.items() if v])
    s.add(Or([p != v for p, v in vals.items()]))
print(sorted(lists))
