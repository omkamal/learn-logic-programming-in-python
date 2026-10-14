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

def ask(form, order):
    for a, b in EDGES:
        +flight(a, b)
    reach(X, Y) <= flight(X, Y)
    if order == 'FIRST':
        reach(X, Y) <= reach(X, Z) & flight(Z, Y)
    else:
        reach(X, Y) <= flight(X, Z) & reach(Z, Y)
    if form == 'where from CAI':
        return len(reach('CAI', Y).data)
    if form == 'who reaches JFK':
        return len(reach(X, 'JFK').data)
    if form == 'every pair':
        return len(reach(X, Y).data)
    return bool(reach('CAI', 'JFK'))          # a yes-or-no question

def show(result):
    status, value = result
    return 'no answer in 5 s' if status == 'timeout' else f'found {value}'

if __name__ == '__main__':
    forms = ['where from CAI', 'who reaches JFK', 'every pair', 'yes or no']
    for form in forms:
        cells = []
        for order in ('FIRST', 'LAST'):
            result = with_timeout(ask, (form, order), 5)
            cells.append(f'{order} {show(result)}')
        print(f'{form}:', ' | '.join(cells), flush=True)
