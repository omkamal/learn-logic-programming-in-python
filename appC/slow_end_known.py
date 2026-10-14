# timeout: 60
# Same chain, same rule, recursive literal first. Only the question moves.
import time
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach')
N = 300
for i in range(N):
    +link(i, i + 1)
reach(X, Y) <= link(X, Y)
reach(X, Y) <= reach(X, Z) & link(Z, Y)

t0 = time.perf_counter()
start_known = len(reach(0, Y).data)             # where can stop 0 go?
t1 = time.perf_counter()
end_known = len(reach(X, N).data)               # who can reach stop 300?
t2 = time.perf_counter()
print(start_known, 'answers when the start is known')
print(end_known, 'answers when the end is known')
print('end known is more than 20 times slower:',
      (t2 - t1) > 20 * (t1 - t0))
