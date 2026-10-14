from functools import reduce
from operator import and_
from pyDatalog import pyDatalog

pyDatalog.create_terms('digit, grid')
for d in range(1, 5):
    +digit(d)

cells = pyDatalog.variables(16)         # cell number = 4 * row + column

def related(a, b):                      # same row, column or 2 x 2 box
    (r1, c1), (r2, c2) = divmod(a, 4), divmod(b, 4)
    same_box = (r1 // 2, c1 // 2) == (r2 // 2, c2 // 2)
    return r1 == r2 or c1 == c2 or same_box

body = []
for b in range(16):
    body.append(digit(cells[b]))
    body += [cells[a] != cells[b] for a in range(b) if related(a, b)]
grid(*cells) <= reduce(and_, body)

print(len(grid(*cells).data), 'complete grids')

given = {0: 1, 3: 4, 5: 3, 10: 1, 12: 3}   # numbers printed in the puzzle
question = [given.get(i, cells[i]) for i in range(16)]
answers = grid(*question).data
print(len(answers), 'grid fits the givens')
free = iter(answers[0])                 # the answer has the blanks only
numbers = [given.get(i) or next(free) for i in range(16)]
for r in range(4):
    print(numbers[4 * r: 4 * r + 4])

# a good puzzle has one solution: what if one printed number is missing?
for dropped in given:
    fewer = {i: v for i, v in given.items() if i != dropped}
    question = [fewer.get(i, cells[i]) for i in range(16)]
    print('without the number in cell', dropped, '->',
          len(grid(*question).data), 'grids')
