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

def reach_from(edges, order, start):
    for a, b in edges:
        +flight(a, b)
    reach(X, Y) <= flight(X, Y)
    if order == 'FIRST':
        reach(X, Y) <= reach(X, Z) & flight(Z, Y)
    else:
        reach(X, Y) <= flight(X, Z) & reach(Z, Y)
    return len(reach(start, Y).data)

RING = [('A', 'B'), ('B', 'C'), ('C', 'A')]
OURS = [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'), ('LHR', 'CAI')]
SQUARE = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]

SHAPES = [
    ('ring of three, all flights one way', RING, 'A'),
    ('the same ring plus a flight B > A', RING + [('B', 'A')], 'A'),
    ('our network, from CAI', OURS, 'CAI'),
    ('our network plus a flight DXB > CAI', OURS + [('DXB', 'CAI')], 'CAI'),
    ('ring of four, all flights one way', SQUARE, 'A'),
    ('the same ring plus a flight B > A', SQUARE + [('B', 'A')], 'A'),
]

def show(result):
    status, value = result
    if status == 'timeout':
        return 'no answer in 5 s'
    return f'found {value}' if status == 'answer' else value

if __name__ == '__main__':
    for name, edges, start in SHAPES:
        cells = []
        for order in ('FIRST', 'LAST'):
            result = with_timeout(reach_from, (edges, order, start), 5)
            cells.append(f'{order} {show(result)}')
        print(f'{name}:', ' | '.join(cells), flush=True)
