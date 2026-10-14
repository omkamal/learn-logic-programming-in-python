parent = [('alice', 'bob'), ('bob', 'carol'), ('carol', 'dave')]

def children(p):
    return [c for (q, c) in parent if q == p]

def parents(p):
    return [q for (q, c) in parent if c == p]

def descendants(p):              # everyone below p: recursion in Python
    found = []
    for c in children(p):
        found.append(c)
        found += descendants(c)
    return found

def ancestors(p):                # the other direction needs a new function
    found = []
    for q in parents(p):
        found.append(q)
        found += ancestors(q)
    return found

print(sorted(descendants('alice')))
print(sorted(ancestors('dave')))
print('dave' in descendants('alice'))
