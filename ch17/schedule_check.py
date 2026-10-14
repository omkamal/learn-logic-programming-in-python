# An independent check of schedule_z3.py: try every start-time plan
# (depth first, giving up on a plan as soon as it breaks a rule).
hours = {"prep": 2, "soup": 3, "roast": 4, "salad": 1, "dessert": 2,
         "plate": 1}
needs = {"soup": ["prep"], "roast": ["prep"], "salad": ["prep"],
         "dessert": ["prep"],
         "plate": ["soup", "roast", "salad", "dessert"]}
order = ["prep", "soup", "roast", "salad", "dessert", "plate"]
LAST = 13                       # no plan needs to start later than 13 hours

def search(cooks):
    best = [None, 0]            # [best finish, number of complete plans]
    busy = [0] * (LAST + 5)     # how many jobs run in each hour so far
    plan = {}
    def place(k):
        if k == len(order):
            best[1] += 1
            finish = max(plan[j] + hours[j] for j in hours)
            best[0] = finish if best[0] is None else min(best[0], finish)
            return
        j = order[k]
        earliest = max([plan[b] + hours[b] for b in needs.get(j, [])] + [0])
        for s in range(earliest, LAST + 1):
            if any(busy[t] >= cooks for t in range(s, s + hours[j])):
                continue
            for t in range(s, s + hours[j]):
                busy[t] += 1
            plan[j] = s
            place(k + 1)
            for t in range(s, s + hours[j]):
                busy[t] -= 1
    place(0)
    return best

for cooks in (1, 2, 3):
    finish, count = search(cooks)
    print(f"{cooks} cook(s): best finish {finish} h, found among "
          f"{count} legal plans")
