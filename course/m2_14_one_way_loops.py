import multiprocessing
import queue
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach')

def run(flights, start, order, box):
    for a, b in flights:
        +flight(a, b)
    reach(X, Y) <= flight(X, Y)
    if order == 'FIRST':
        reach(X, Y) <= reach(X, Z) & flight(Z, Y)
    else:
        reach(X, Y) <= flight(X, Z) & reach(Z, Y)
    box.put(sorted(y for (y,) in reach(start, Y).data))

RING3 = [('A', 'B'), ('B', 'C'), ('C', 'A')]               # a one-way loop of 3
RING4 = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]   # a one-way loop of 4
OURS = [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'CAI'), ('LHR', 'JFK')]

SHAPES = [
    ('ring of 3, one-way', RING3, 'A'),
    ('ring of 3 + B>A', RING3 + [('B', 'A')], 'A'),         # one flight the opposite way
    ('ring of 4, one-way', RING4, 'A'),
    ('ring of 4 + B>A', RING4 + [('B', 'A')], 'A'),
    ('course network, from CAI', OURS, 'CAI'),
    ('course network + DXB>CAI', OURS + [('DXB', 'CAI')], 'CAI'),
    ('course network, from JFK', OURS, 'JFK'),             # the loop is not reachable from JFK
]

if __name__ == '__main__':
    for name, flights, start in SHAPES:
        row = []
        for order in ('FIRST', 'LAST'):
            box = multiprocessing.Queue()
            child = multiprocessing.Process(target=run, args=(flights, start, order, box))
            child.start()
            try:
                cities = box.get(timeout=5)            # wait at most 5 seconds
                child.join()
                row.append(f'{order}: {cities}')
            except queue.Empty:
                child.kill()
                child.join()
                row.append(f'{order}: no answer after 5 s')
        print(f'{name}:', ' | '.join(row), flush=True)
