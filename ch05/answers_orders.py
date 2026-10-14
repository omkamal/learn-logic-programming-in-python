# timeout: 60
import multiprocessing
from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, C, P, P1, P2, fare, trip')

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

def try_variant(v):
    for a, b, p in [('CAI', 'DXB', 150), ('DXB', 'LHR', 320),
                    ('LHR', 'JFK', 410), ('LHR', 'CAI', 180)]:
        +fare(a, b, p)
    f1, f2 = fare(A, B, P1), fare(B, C, P2)
    total, small = (P == P1 + P2), (P < 700)
    if v == 'a':
        trip(A, C, P) <= f1 & f2 & total & small
    elif v == 'b':
        trip(A, C, P) <= f2 & f1 & small & total
    elif v == 'c':
        trip(A, C, P) <= f2 & f1 & total & small
    elif v == 'd':
        trip(A, C, P) <= f1 & total & f2 & small
    else:
        trip(A, C, P) <= small & f1 & f2 & total
    return sorted(trip(A, C, P).data)

if __name__ == '__main__':
    for v in 'abcde':
        print(v, with_timeout(try_variant, (v,), 5))
