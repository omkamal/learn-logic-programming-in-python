from pyDatalog import pyDatalog

links = {('CAI', 'DXB'): 4, ('DXB', 'LHR'): 7, ('CAI', 'LHR'): 12,
         ('LHR', 'JFK'): 8, ('DXB', 'JFK'): 14}


def show(cards):
    return ' '.join(f'{a}>{b}:{c}' for a, b, c in sorted(cards))


notebook = {(a, b, c) for (a, b), c in links.items()}
print('round 1:', show(notebook))
rnd = 1
while True:
    new = {(x, y, c1 + c2)
           for (x, z, c1) in notebook
           for (z2, y), c2 in links.items() if z == z2} - notebook
    rnd += 1
    print(f'round {rnd}:', show(new))
    if not new:
        break
    notebook |= new

pyDatalog.create_terms('X, Y, C, C1, C2, Z, link, path')
for (a, b), c in links.items():
    +link(a, b, c)
path(X, Y, C) <= link(X, Y, C)
path(X, Y, C) <= path(X, Z, C1) & link(Z, Y, C2) & (C == C1 + C2)
print(len(notebook), 'cards; same as the engine:',
      notebook == set(path(X, Y, C).data))
