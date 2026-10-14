# timeout: 60
import multiprocessing
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, can_reach')

def run_job(job, args, box):          # this runs inside the new process
    try:
        box.put(('answer', job(*args)))
    except Exception as err:
        box.put(('error', type(err).__name__))

def with_timeout(job, args, seconds):
    box = multiprocessing.Queue()
    child = multiprocessing.Process(target=run_job, args=(job, args, box))
    child.start()
    child.join(seconds)               # wait at most this many seconds
    if child.is_alive():              # still busy: it is hanging
        child.kill()
        child.join()
        return ('timeout', None)
    return box.get()

def tutorial(two_way):
    # the links of the pyDatalog tutorial (a loop: 2 > 5 > 6 > 7 > 2)
    for a, b in [(1, 2), (2, 3), (2, 4), (2, 5), (5, 6), (6, 7), (7, 2)]:
        +link(a, b)
    if two_way:
        link(X, Y) <= link(Y, X)      # the tutorial: two-way links
    can_reach(X, Y) <= link(X, Y)
    can_reach(X, Y) <= link(X, Z) & can_reach(Z, Y) & (X != Y)  # last
    return sorted(y for (y,) in can_reach(1, Y).data)

if __name__ == '__main__':
    for name, two_way in [('every link also goes back', True),
                          ('links go one way only', False)]:
        status, value = with_timeout(tutorial, (two_way,), 5)
        shown = value if status == 'answer' else 'no answer in 5 s'
        print(f'{name}:', shown)
