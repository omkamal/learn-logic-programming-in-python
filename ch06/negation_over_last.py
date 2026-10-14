# timeout: 60
import multiprocessing
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, city, reach, unreachable')

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
    if child.is_alive():              # no answer in time: stop it
        child.kill()
        child.join()
        return ('timeout', None)
    return box.get()

def not_reached(order):
    for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'JFK'),
                 ('LHR', 'CAI')]:
        +flight(a, b)
    for c in ['CAI', 'DXB', 'LHR', 'JFK', 'NRT']:
        +city(c)
    reach(X, Y) <= flight(X, Y)
    if order == 'FIRST':
        reach(X, Y) <= reach(X, Z) & flight(Z, Y)
    else:
        reach(X, Y) <= flight(X, Z) & reach(Z, Y)
    unreachable(Y) <= city(Y) & ~reach('CAI', Y)
    return sorted(unreachable(Y).data)

if __name__ == '__main__':
    for order in ('FIRST', 'LAST'):
        status, value = with_timeout(not_reached, (order,), 5)
        print(f'reach with the recursive literal {order}:',
              value if status == 'answer' else 'no answer in 5 s')
