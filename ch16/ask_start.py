import time
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach, reach_last, reached_by')

def fresh(n):
    pyDatalog.clear()
    for i in range(n):
        +link(i, i + 1)
    reach(X, Y) <= link(X, Y)
    reach(X, Y) <= reach(X, Z) & link(Z, Y)
    reach_last(X, Y) <= link(X, Y)
    reach_last(X, Y) <= link(X, Z) & reach_last(Z, Y)
    reached_by(Y, X) <= link(X, Y)                  # the mirror image
    reached_by(Y, X) <= reached_by(Y, Z) & link(X, Z)

def timed(label, question):
    fresh(800)
    start = time.perf_counter()
    answers = len(question().data)
    seconds = time.perf_counter() - start
    print('%-34s %8d %8.3f' % (label, answers, seconds))

print('%-34s %8s %8s' % ('question', 'answers', 'seconds'))
timed('reach(0, Y)         start known', lambda: reach(0, Y))
timed('reached_by(800, X)  end known', lambda: reached_by(800, X))
timed('reach(0, 800)       yes or no', lambda: reach(0, 800))
timed('reach(X, 800)       end known', lambda: reach(X, 800))
timed('reach(X, Y)         nothing known', lambda: reach(X, Y))
timed('reach_last(0, Y)    start known', lambda: reach_last(0, Y))
