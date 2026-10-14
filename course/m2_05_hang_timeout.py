import multiprocessing
import resource
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach')
for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'CAI'), ('LHR', 'JFK')]:
    +flight(a, b)
reach(X, Y) <= flight(X, Y)

def first():
    reach(X, Y) <= reach(X, Z) & flight(Z, Y)   # recursive literal FIRST
    print('FIRST:', sorted(reach('CAI', Y).data), flush=True)

def last():
    reach(X, Y) <= flight(X, Z) & reach(Z, Y)   # recursive literal LAST
    print('LAST:', sorted(reach('CAI', Y).data), flush=True)

if __name__ == '__main__':
    for run in (first, last):
        cpu_before = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
        child = multiprocessing.Process(target=run)   # a process we are allowed to stop
        child.start()
        child.join(timeout=10)                        # wait at most 10 seconds
        if child.is_alive():
            child.kill()
            child.join()
            cpu = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime - cpu_before
            print(f'{run.__name__.upper()}: no answer and no error after 10 s; it used {cpu:.1f} s of CPU', flush=True)
