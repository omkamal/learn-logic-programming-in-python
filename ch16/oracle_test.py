import random
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach')

def closure(links):
    """The slow, obviously correct version: plain Python, round by round."""
    pairs = set(links)
    while True:
        new = {(a, d) for (a, b) in pairs for (c, d) in links if b == c}
        if new <= pairs:
            return pairs
        pairs |= new

random.seed(7)
for trial in range(300):
    links = {(random.randrange(6), random.randrange(6))
             for _ in range(random.randrange(1, 12))}
    pyDatalog.clear()
    reach(X, Y) <= link(X, Y)
    reach(X, Y) <= reach(X, Z) & link(Z, Y)
    for a, b in links:
        +link(a, b)
    assert set(reach(X, Y).data) == closure(links), sorted(links)
print('300 random small graphs: rules and plain Python agree')
