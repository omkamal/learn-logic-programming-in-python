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

def reach_around(n, order):           # a loop of n airports A > B > ... > A
    names = 'ABCDEFGH'[:n]
    for i in range(n):
        +flight(names[i], names[(i + 1) % n])
    reach(X, Y) <= flight(X, Y)
    if order == 'FIRST':
        reach(X, Y) <= reach(X, Z) & flight(Z, Y)
    else:
        reach(X, Y) <= flight(X, Z) & reach(Z, Y)
    return len(reach('A', Y).data)

def show(result, seconds):
    status, value = result
    if status == 'timeout':
        return f'no answer in {seconds} s'
    return f'found {value}' if status == 'answer' else value

if __name__ == '__main__':
    for n in range(1, 9):
        cells = []
        for order in ('FIRST', 'LAST'):
            result = with_timeout(reach_around, (n, order), 5)
            cells.append(f'{order}: {show(result, 5)}')
        print(f'loop of {n}:', ' | '.join(cells), flush=True)
