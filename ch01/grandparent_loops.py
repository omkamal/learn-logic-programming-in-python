# The clerk with the manual: every step spelled out.
parents = [("alice", "bob"), ("alice", "carol"),
           ("bob", "dave"), ("carol", "erin")]

grandparents = []
for (a, b) in parents:            # for every parent card ...
    for (c, d) in parents:        # ... look at every other parent card
        if b == c:                # the child of the first is the
            grandparents.append((a, d))   # parent of the second

print(sorted(grandparents))
