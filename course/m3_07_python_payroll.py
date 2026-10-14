rows = [('ann', 'eng', 120), ('bob', 'eng', 100), ('cid', 'ops', 80),
        ('dee', 'ops', 90), ('eli', 'hr', 70)]

# plain Python: one loop, three dictionaries to keep in sync
headcount, total, top = {}, {}, {}
for name, dept, salary in rows:
    headcount[dept] = headcount.get(dept, 0) + 1
    total[dept] = total.get(dept, 0) + salary
    if dept not in top or salary > top[dept][1]:
        top[dept] = (name, salary)

print(sorted(headcount.items()))
print(sorted(total.items()))
print(sorted((d, n) for d, (n, s) in top.items()))
