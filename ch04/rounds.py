from pyDatalog import pyDatalog

parent_facts = [('alice', 'bob'), ('bob', 'carol'), ('carol', 'dave')]

# 1. the notebook, by hand, in plain Python (the textbook meaning)
notebook = set(parent_facts)         # round 1: the base case
print('round 1:', sorted(notebook))
n = 1
while True:
    n += 1
    # recursive clause: a card in the notebook + one parent card
    new = {(x, y) for (x, z) in notebook
                  for (z2, y) in parent_facts if z == z2} - notebook
    print(f'round {n}:', sorted(new))
    if not new:                      # a quiet round: stop
        break
    notebook |= new

# 2. the same question asked of pyDatalog
pyDatalog.create_terms('X, Y, Z, parent, ancestor')
for a, b in parent_facts:
    +parent(a, b)
ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= ancestor(X, Z) & parent(Z, Y)

engine = set(ancestor(X, Y).data)
print('same answers as the engine:', notebook == engine)
