# A dinner to cook: six jobs, some must wait for others, a few cooks.
# Z3's Optimize asks for the earliest possible finish.
from z3 import Int, If, And, Sum, Optimize, sat

hours = {"prep": 2, "soup": 3, "roast": 4, "salad": 1, "dessert": 2,
         "plate": 1}
needs = {"soup": ["prep"], "roast": ["prep"], "salad": ["prep"],
         "dessert": ["prep"],
         "plate": ["soup", "roast", "salad", "dessert"]}

def best_schedule(cooks):
    start = {j: Int(j) for j in hours}
    end = Int("end")
    opt = Optimize()
    for j, h in hours.items():
        opt.add(start[j] >= 0, end >= start[j] + h)     # nothing before 0
    for j, before in needs.items():
        for b in before:
            opt.add(start[j] >= start[b] + hours[b])    # wait for them
    for t in range(sum(hours.values())):                # in every hour, at
        running = [If(And(start[j] <= t, t < start[j] + h), 1, 0)
                   for j, h in hours.items()]           # most `cooks` jobs
        opt.add(Sum(running) <= cooks)
    opt.minimize(end)                                   # finish as early as
    assert opt.check() == sat                           # possible
    m = opt.model()
    return m[end].as_long(), {j: m[start[j]].as_long() for j in hours}

for cooks in (1, 2, 3):
    finish, plan = best_schedule(cooks)
    print(f"{cooks} cook(s): done after {finish} hours")
    if cooks == 2:
        for j in sorted(plan, key=lambda j: (plan[j], j)):
            print(f"    hour {plan[j]}: start {j} ({hours[j]} h)")
