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
    child.join(seconds)
    if child.is_alive():
        child.kill()
        child.join()
        return ('timeout', None)
    return box.get()

def last_from(edges, start):          # recursive literal LAST
    for a, b in edges:
        +flight(a, b)
    reach(X, Y) <= flight(X, Y)
    reach(X, Y) <= flight(X, Z) & reach(Z, Y)
    return len(reach(start, Y).data)

CASES = {
    'a': ([('A', 'B'), ('B', 'A')], 'A'),
    'b': ([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], 'A'),
    'c': ([('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'A')], 'D'),
    'd': ([('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'E')], 'D'),
}

if __name__ == '__main__':
    for name, (edges, start) in CASES.items():
        status, value = with_timeout(last_from, (edges, start), 5)
        print(name, status, value)
