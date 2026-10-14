# timeout: 120
import itertools
import multiprocessing
from pyDatalog import pyDatalog

pyDatalog.create_terms('M, B, D, F, late, fee')

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

NAMES = ['fill', 'calculate', 'check']

def try_order(order):
    for m, b, d in [('mia', 'atlas', 3), ('noor', 'poems', 6),
                    ('omar', 'maps', 2)]:
        +late(m, b, d)
    parts = {'fill': late(M, B, D),        # a table: fills M, B, D
             'calculate': (F == D * 25),   # 25 cents a day: needs D
             'check': (F > 100)}           # needs F
    first, second, third = (parts[name] for name in order)
    fee(M, B, F) <= first & second & third
    return sorted(fee(M, B, F).data)

if __name__ == '__main__':
    for order in itertools.permutations(NAMES):
        status, value = with_timeout(try_order, (order,), 5)
        print(', '.join(order), '->', value)
