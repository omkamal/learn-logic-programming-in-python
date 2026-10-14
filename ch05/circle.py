# timeout: 60
import multiprocessing
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, follows, network')

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

def network_of(edges, order, who):
    for a, b in edges:
        +follows(a, b)
    network(X, Y) <= follows(X, Y)
    if order == 'FIRST':
        network(X, Y) <= network(X, Z) & follows(Z, Y)
    else:
        network(X, Y) <= follows(X, Z) & network(Z, Y)
    return [y for (y,) in sorted(network(who, Y).data)]

PAIR = [('ana', 'ben'), ('ben', 'ana')]
RING = [('ana', 'ben'), ('ben', 'cy'), ('cy', 'ana')]

if __name__ == '__main__':
    for name, edges in [('two friends', PAIR), ('three friends', RING)]:
        for order in ('FIRST', 'LAST'):
            job = (edges, order, 'ana')
            status, value = with_timeout(network_of, job, 5)
            print(f'{name}, {order}:', value or 'no answer in 5 s')
