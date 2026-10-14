# A one-room day: four meetings, unknown start hours, Z3 finds a timetable.
from itertools import combinations
from z3 import Int, Solver, Or, sat

hours = {"standup": 1, "design": 2, "review": 1, "demo": 2}   # lengths
start = {name: Int(name) for name in hours}                   # the unknowns

s = Solver()
for name, h in hours.items():
    s.add(start[name] >= 9, start[name] + h <= 17)     # inside 9:00-17:00
    s.add(Or(start[name] + h <= 12, start[name] >= 13))   # none at lunch
for a, b in combinations(hours, 2):                 # one room: no overlap
    s.add(Or(start[a] + hours[a] <= start[b],
             start[b] + hours[b] <= start[a]))
s.add(start["standup"] == 9)                        # standup opens the day
s.add(start["design"] < start["review"])            # design, then review,
s.add(start["review"] < start["demo"])              # then the demo

print(s.check())
m = s.model()
for name in sorted(hours, key=lambda n: m[start[n]].as_long()):
    t = m[start[name]].as_long()
    print(f"{t:2d}:00-{t + hours[name]:2d}:00  {name}")

s.push()                                  # a what-if, easy to undo
s.add(start["demo"] + hours["demo"] <= 14)
print("demo must end by 14:00 ->", s.check())
s.pop()

count = 0                                 # how many timetables are there?
while s.check() == sat:
    m = s.model()
    count += 1
    s.add(Or([start[n] != m[start[n]] for n in hours]))
print("timetables in all:", count)
