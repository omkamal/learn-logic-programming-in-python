# The same access policy, checked by Z3: "is there ANY request that
# breaks rule R?"
from z3 import Const, EnumSort, And, Or, Not, Solver, sat

User, users = EnumSort("User", ["maya", "noor", "omar", "pat"])
Action, actions = EnumSort("Action", ["read", "write", "delete"])
U = dict(zip(["maya", "noor", "omar", "pat"], users))
A = dict(zip(["read", "write", "delete"], actions))

# The policy data, exactly as in policy_pydatalog.py.
has_role = {"maya": "admin", "noor": "editor", "omar": "viewer",
            "pat": "editor"}
inherits = {"admin": "editor", "editor": "viewer"}   # admin > ...
role_perm = {"viewer": ["read"], "editor": ["write"], "admin": ["delete"]}

def roles_below(role):            # the role itself and what it inherits
    while True:
        yield role
        if role not in inherits:
            return
        role = inherits[role]

def can(u, a, blocked):           # the policy as ONE logical formula
    granted = [And(u == U[n], a == A[p])
               for n, r in has_role.items()
               for r2 in roles_below(r) for p in role_perm[r2]]
    stopped = [And(u == U[n], a == A[p]) for n, p in blocked]
    return And(Or(granted), Not(Or(stopped)))

u, a = Const("u", User), Const("a", Action)     # the UNKNOWN request

def search(rule_name, broken, blocked):
    s = Solver()
    s.add(can(u, a, blocked), broken)           # allowed AND breaks R
    if s.check() == sat:
        who, what = s.model()[u], s.model()[a]
        print(f"{rule_name}: yes, for example {who} may {what}")
    else:
        print(f"{rule_name}: no request breaks it")

viewers = [n for n, r in has_role.items() if r == "viewer"]
r1 = And(u == U["pat"], a == A["write"])        # R1: pat may never write
r2 = And(Or([u == U[n] for n in viewers]), a != A["read"])   # R2

print("policy as given:")
search("  R1", r1, blocked=[("pat", "write")])
search("  R2", r2, blocked=[("pat", "write")])
print("after somebody lifts pat's block:")
search("  R1", r1, blocked=[])
search("  R2", r2, blocked=[])
