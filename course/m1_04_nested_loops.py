# The "before" picture: grandparents and siblings with plain Python loops
parents = [('alice', 'bob'), ('alice', 'carol'),
           ('bob', 'dave'), ('carol', 'erin')]
people = ['alice', 'bob', 'carol', 'dave', 'erin']

grandparents = []
for person in people:
    for (p, child) in parents:
        if p == person:
            for (c, grandchild) in parents:
                if c == child:
                    grandparents.append((person, grandchild))
print(grandparents)

siblings = []
for (p1, a) in parents:
    for (p2, b) in parents:
        if p1 == p2 and a != b:
            siblings.append((a, b))
print(siblings)
