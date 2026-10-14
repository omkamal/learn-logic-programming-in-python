# The family cards as a plain Python list, one function per question
cards = [('alice', 'bob'), ('alice', 'carol'),
         ('bob', 'dave'), ('carol', 'erin')]


def children_of(person):
    return [c for (p, c) in cards if p == person]


def parents_of(person):
    return [p for (p, c) in cards if c == person]


print(children_of('alice'))
print(parents_of('dave'))
print(cards)
