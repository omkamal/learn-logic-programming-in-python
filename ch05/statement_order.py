# timeout: 120
import multiprocessing
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach')

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

EDGES = [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'), ('LHR', 'CAI')]

def ask(variant):
    for a, b in EDGES:
        +flight(a, b)
    if variant == 1:        # base clause, then recursive literal FIRST
        reach(X, Y) <= flight(X, Y)
        reach(X, Y) <= reach(X, Z) & flight(Z, Y)
    elif variant == 2:      # the same two clauses, swapped
        reach(X, Y) <= reach(X, Z) & flight(Z, Y)
        reach(X, Y) <= flight(X, Y)
    elif variant == 3:      # base clause, then recursive literal LAST
        reach(X, Y) <= flight(X, Y)
        reach(X, Y) <= flight(X, Z) & reach(Z, Y)
    elif variant == 4:      # the same two clauses, swapped
        reach(X, Y) <= flight(X, Z) & reach(Z, Y)
        reach(X, Y) <= flight(X, Y)
    else:                   # two recursive literals
        reach(X, Y) <= flight(X, Y)
        reach(X, Y) <= reach(X, Z) & reach(Z, Y)
    return len(reach('CAI', Y).data)

NAMES = {1: 'base clause, then FIRST       ',
         2: 'FIRST, then base clause       ',
         3: 'base clause, then LAST        ',
         4: 'LAST, then base clause        ',
         5: 'base clause, then reach & reach'}

if __name__ == '__main__':
    for variant in (1, 2, 3, 4, 5):
        status, value = with_timeout(ask, (variant,), 5)
        text = f'found {value}'
        if status == 'timeout':
            text = 'no answer in 5 s'
        print(NAMES[variant], text, flush=True)
