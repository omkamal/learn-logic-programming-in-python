# SAT in miniature: three yes/no unknowns and three rules about a party.
from itertools import product
from z3 import Bools, Implies, And, Or, Not, Solver, sat

people = ("ann", "bob", "cid")
ann, bob, cid = Bools(" ".join(people))       # does each person come?
rules = [
    Implies(ann, bob),                        # Ann comes only if Bob comes
    Not(And(bob, cid)),                       # Bob and Cid never together
    Or(ann, bob, cid),                        # somebody comes
]

def who(guests):                              # (True, False, ..) -> names
    return [p for p, comes in zip(people, guests) if comes]

def all_guest_lists(extra=()):
    s = Solver()
    s.add(*rules, *extra)
    found = []
    while s.check() == sat:
        m = s.model()
        vals = [m.eval(p, model_completion=True) for p in (ann, bob, cid)]
        found.append(who(bool(v) for v in vals))
        s.add(Or([p != v for p, v in zip((ann, bob, cid), vals)]))
    return found

print("rules only:       ", sorted(all_guest_lists()))
print("and Cid must come:", all_guest_lists([cid]))
print("Ann and Cid both: ", all_guest_lists([ann, cid]))

# The same list by brute force: try all 2 * 2 * 2 = 8 guest lists.
ok = [who(g) for g in product([False, True], repeat=3)
      if (not g[0] or g[1]) and not (g[1] and g[2]) and any(g)]
print("brute force:      ", sorted(ok))
