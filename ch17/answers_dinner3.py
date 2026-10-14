# Answer to exercise 5: the dinner with a three-hour dessert.
from z3 import Int, If, And, Sum, Optimize, sat

hours = {"prep": 2, "soup": 3, "roast": 4, "salad": 1, "dessert": 3,
         "plate": 1}
needs = {"soup": ["prep"], "roast": ["prep"], "salad": ["prep"],
         "dessert": ["prep"],
         "plate": ["soup", "roast", "salad", "dessert"]}

for cooks in (1, 2, 3):
    start = {j: Int(j) for j in hours}
    end = Int("end")
    opt = Optimize()
    for j, h in hours.items():
        opt.add(start[j] >= 0, end >= start[j] + h)
    for j, before in needs.items():
        for b in before:
            opt.add(start[j] >= start[b] + hours[b])
    for t in range(sum(hours.values())):
        running = [If(And(start[j] <= t, t < start[j] + h), 1, 0)
                   for j, h in hours.items()]
        opt.add(Sum(running) <= cooks)
    opt.minimize(end)
    assert opt.check() == sat
    print(f"{cooks} cook(s): done after {opt.model()[end]} hours")
