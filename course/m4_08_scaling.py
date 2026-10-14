import resource
import time
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach')

# a straight chain 0 -> 1 -> 2 -> ... -> n, then every reachable pair
for n in [100, 200, 400, 800]:
    pyDatalog.clear()
    for i in range(n):
        +link(i, i + 1)
    reach(X, Y) <= link(X, Y)
    reach(X, Y) <= reach(X, Z) & link(Z, Y)
    t = time.perf_counter()
    pairs = len(reach(X, Y).data)
    secs = round(time.perf_counter() - t, 2)
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024
    print(n, 'links ->', pairs, 'pairs in', secs, 's, peak', peak, 'MB')
