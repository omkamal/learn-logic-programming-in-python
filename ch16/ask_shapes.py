import time
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach')

def timed(label, links, start):
    pyDatalog.clear()
    for a, b in links:
        +link(a, b)
    reach(X, Y) <= link(X, Y)
    reach(X, Y) <= reach(X, Z) & link(Z, Y)
    clock = time.perf_counter()
    answers = len(reach(start, Y).data)
    seconds = time.perf_counter() - clock
    print('%-26s %6d answers %7.3f s' % (label, answers, seconds))

ring = [(i, (i + 1) % 800) for i in range(800)]
tree = [(i // 2, i) for i in range(2, 8192)]
timed('ring of 800, start known', ring, 0)
timed('tree of 8191, root known', tree, 1)
