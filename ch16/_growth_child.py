# one run of the "all pairs" test, in its own process (clean memory count)
import resource
import sys
import time
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach')

shape, n = sys.argv[1], int(sys.argv[2])
if shape == 'chain':
    links = [(i, i + 1) for i in range(n)]
elif shape == 'ring':
    links = [(i, (i + 1) % n) for i in range(n)]
else:                                  # a complete binary tree, nodes 1..n
    links = [(i // 2, i) for i in range(2, n + 1)]

for a, b in links:
    +link(a, b)
reach(X, Y) <= link(X, Y)
reach(X, Y) <= reach(X, Z) & link(Z, Y)

start = time.perf_counter()
pairs = len(reach(X, Y).data)
seconds = time.perf_counter() - start
peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024
print(shape, len(links), pairs, seconds, peak)
