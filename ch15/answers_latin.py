from functools import reduce
from operator import and_
from pyDatalog import pyDatalog

pyDatalog.create_terms('digit, grid')
for d in range(1, 5):
    +digit(d)

cells = pyDatalog.variables(16)         # cell number = 4 * row + column

def related(a, b):                      # same row or same column only
    return a // 4 == b // 4 or a % 4 == b % 4

body = []
for b in range(16):
    body.append(digit(cells[b]))
    body += [cells[a] != cells[b] for a in range(b) if related(a, b)]
grid(*cells) <= reduce(and_, body)

print(len(grid(*cells).data), 'grids without the box rule')
