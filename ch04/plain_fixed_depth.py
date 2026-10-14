def three_deep(parent):
    found = set()
    for (a, b) in parent:
        found.add((a, b))                    # one step
        for (b2, c) in parent:
            if b == b2:
                found.add((a, c))            # two steps
                for (c2, d) in parent:
                    if c == c2:
                        found.add((a, d))    # three steps
    return found

parent = [('alice', 'bob'), ('bob', 'carol'), ('carol', 'dave')]
print(len(three_deep(parent)), 'pairs')

parent.append(('dave', 'eve'))               # the family grows
found = three_deep(parent)
print(len(found), 'pairs; alice-eve found?', ('alice', 'eve') in found)
