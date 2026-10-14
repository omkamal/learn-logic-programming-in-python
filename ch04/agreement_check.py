# Not shown in the chapter: notebook vs engine, recursive literal first
# vs last, on every loop-free data set used in Chapter 4.
from pyDatalog import pyDatalog

datasets = {
    'family line': [('alice', 'bob'), ('bob', 'carol'),
                    ('carol', 'dave')],
    'branching tree': [('alice', 'bob'), ('alice', 'carol'),
                       ('bob', 'dave'), ('carol', 'erin')],
    'line of five': [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')],
    'flights': [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK')],
    'folders': [('projects', 'web'), ('projects', 'data'),
                ('projects', 'notes.txt'), ('web', 'css'),
                ('web', 'img'), ('web', 'index.html'),
                ('css', 'main.css'), ('img', 'logo.png'),
                ('data', 'raw'), ('data', 'report.pdf'),
                ('raw', 'sales.csv')],
    'prerequisites': [('structures', 'programming'),
                      ('discrete', 'programming'),
                      ('algorithms', 'structures'),
                      ('algorithms', 'discrete'),
                      ('databases', 'structures'),
                      ('learning', 'algorithms'),
                      ('learning', 'statistics')],
    'rumors': [('mia', 'noor'), ('mia', 'omar'), ('noor', 'pat'),
                ('omar', 'quinn'), ('pat', 'ravi'), ('quinn', 'sam'),
                ('tess', 'pat')],
}

def notebook(edges):
    cards, rounds = set(edges), 1
    while True:
        new = {(x, y) for (x, z) in cards
                      for (z2, y) in edges if z == z2} - cards
        if not new:
            return cards, rounds
        cards |= new
        rounds += 1

pyDatalog.create_terms('X, Y, Z')
g = globals()
for i, (name, edges) in enumerate(datasets.items()):
    pyDatalog.create_terms(f'e{i}, first{i}, last{i}')
    e, first, last = g[f'e{i}'], g[f'first{i}'], g[f'last{i}']
    for a, b in edges:
        +e(a, b)
    first(X, Y) <= e(X, Y)
    first(X, Y) <= first(X, Z) & e(Z, Y)
    last(X, Y) <= e(X, Y)
    last(X, Y) <= e(X, Z) & last(Z, Y)
    cards, rounds = notebook(edges)
    f_set, l_set = set(first(X, Y).data), set(last(X, Y).data)
    print(f'{name:15} cards={len(cards):2} rounds={rounds}',
          'notebook=first:', cards == f_set,
          ' first=last:', f_set == l_set)
