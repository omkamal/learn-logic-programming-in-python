# The same approval policy in Z3, where the amount is an UNKNOWN integer.
from z3 import Int, And, Or, Solver, Optimize, sat

amt = Int("amt")                       # any whole number at all

def approve(admin_cap):
    """True when somebody may approve amt: editors up to 1000, admins
    up to admin_cap (None means no limit at all)."""
    editor = And(amt >= 0, amt <= 1000)
    admin = And(amt >= 0, amt <= admin_cap) if admin_cap else amt >= 0
    return Or(editor, admin)

for label, cap in [("admins unlimited", None),
                   ("admins capped at 5000", 5000)]:
    print(label)
    s = Solver()                       # R broken = approved AND above 5000
    s.add(approve(cap), amt > 5000)
    if s.check() == sat:
        print("  R can be broken, for example with amt =", s.model()[amt])
    else:
        print("  no amount breaks R (for every whole number)")
    o = Optimize()                     # the largest amount allowed
    o.add(approve(cap))
    top = o.maximize(amt)
    o.check()
    print("  largest approvable amount:", top.upper())
