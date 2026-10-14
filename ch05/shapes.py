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

SHAPES = [
    ('a diamond, no loop', [('A', 'B'), ('A', 'C'), ('B', 'D'),
                            ('C', 'D')], 'A'),
    ('an airport with a flight to itself', [('A', 'A')], 'A'),
    ('two airports, round trip', [('A', 'B'), ('B', 'A')], 'A'),
    ('round trip plus a tail', [('A', 'B'), ('B', 'A'), ('B', 'C')], 'A'),
    ('a path leading into a round trip', [('S', 'A'), ('A', 'B'),
                                          ('B', 'A')], 'S'),
    ('two round trips joined', [('A', 'B'), ('B', 'A'), ('B', 'C'),
                                ('C', 'B')], 'A'),
    ('three airports in a ring', [('A', 'B'), ('B', 'C'), ('C', 'A')], 'A'),
    ('our network, from CAI', [('CAI', 'DXB'), ('DXB', 'LHR'),
                               ('LHR', 'JFK'), ('LHR', 'CAI')], 'CAI'),
    ('our network, from JFK', [('CAI', 'DXB'), ('DXB', 'LHR'),
                               ('LHR', 'JFK'), ('LHR', 'CAI')], 'JFK'),
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
