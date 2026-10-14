# timeout: 60
import multiprocessing
from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, P, T, X, Y, Z, fare, flight, reach')
pyDatalog.create_terms('cheap, total')

def run_job(job, args, box):          # this runs inside the new process
    try:
        box.put(('answer', job(*args)))
    except Exception as err:
        box.put(('error', type(err).__name__ + ': ' +
                 str(err).splitlines()[0]))

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

def comparison_first():
    +fare('CAI', 'DXB', 150)
    cheap(A, B) <= (P < 200) & fare(A, B, P)
    return sorted(cheap(A, B).data)

def calculation_first():
    +fare('CAI', 'DXB', 150)
    total(A, B, T) <= (T == P + 25) & fare(A, B, P)
    return sorted(total(A, B, T).data)

def recursion_last():
    for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'CAI')]:
        +flight(a, b)
    reach(X, Y) <= flight(X, Y)
    reach(X, Y) <= flight(X, Z) & reach(Z, Y)
    return sorted(reach('CAI', Y).data)

if __name__ == '__main__':
    for name, job in [('comparison first ', comparison_first),
                      ('calculation first', calculation_first),
                      ('recursion last   ', recursion_last)]:
        status, value = with_timeout(job, (), 5)
        if status == 'answer':
            print(name, '-> answer', value)
        elif status == 'error':
            print(name, '-> error:')
            print('   ', value)
        else:
            print(name, '-> no answer in 5 s')
