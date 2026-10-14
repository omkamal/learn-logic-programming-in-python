rows = [('ann', 'eng', 120), ('bob', 'eng', 100), ('cid', 'ops', 80),
        ('dee', 'ops', 90), ('eli', 'hr', 70)]

by_dept = {}
for name, dept, pay in rows:
    by_dept.setdefault(dept, []).append((pay, name))

place = {}
for dept, people in by_dept.items():
    for i, (pay, name) in enumerate(sorted(people, reverse=True)):
        place[name] = i

print(sorted(place.items()))
