rows = [('ann', 'eng', 120), ('bob', 'eng', 100), ('cid', 'ops', 80),
        ('dee', 'ops', 90), ('eli', 'hr', 70)]

# step 1: sort every row into the basket of its department
baskets = {}
for name, dept, salary in rows:
    baskets.setdefault(dept, []).append((name, salary))
for dept in sorted(baskets):
    print(dept, baskets[dept])

# step 2: summarize each basket on its own
for dept in sorted(baskets):
    pay = [salary for name, salary in baskets[dept]]
    print(dept, 'total', sum(pay), 'people', len(pay), 'top', max(pay))
