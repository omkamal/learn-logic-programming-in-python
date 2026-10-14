# timeout: 60
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

def reach_from(edges, order, start):
    for a, b in edges:
        +flight(a, b)
    reach(X, Y) <= flight(X, Y)
    if order == 'FIRST':
        reach(X, Y) <= reach(X, Z) & flight(Z, Y)
    else:
        reach(X, Y) <= flight(X, Z) & reach(Z, Y)
    return sorted(reach(start, Y).data)

if __name__ == '__main__':
    # the start method of Windows and macOS, forced on any system
    multiprocessing.set_start_method('spawn')
    line = [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK')]
    loop = line + [('LHR', 'CAI')]
    for edges in (line, loop):
        for order in ('FIRST', 'LAST'):
            result = with_timeout(reach_from, (edges, order, 'CAI'), 4)
            print(len(edges), 'flights', order, result[0], result[1])
