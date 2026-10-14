import sys
import time
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach')

n = 50000                              # a chain of 50,000 links
for i in range(n):
    +link(i, i + 1)
reach(X, Y) <= link(X, Y)
reach(X, Y) <= reach(X, Z) & link(Z, Y)

start = time.perf_counter()
print('pyDatalog:', len(reach(0, Y).data), 'answers in',
      round(time.perf_counter() - start, 1), 's')

# the same chain, followed by an ordinary recursive Python function
next_of = {i: i + 1 for i in range(n)}

def below(i):
    return [next_of[i]] + below(next_of[i]) if i in next_of else []

print('Python recursion limit:', sys.getrecursionlimit())
try:
    print('Python:', len(below(0)), 'answers')
except RecursionError as error:
    print('Python: RecursionError:', error)
