# timeout: 60
import multiprocessing
import time
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach')

def last():
    for a, b in [('CAI', 'DXB'), ('DXB', 'LHR'), ('LHR', 'CAI'),
                 ('LHR', 'JFK')]:
        +flight(a, b)
    reach(X, Y) <= flight(X, Y)
    reach(X, Y) <= flight(X, Z) & reach(Z, Y)    # recursive literal LAST
    print(sorted(reach('CAI', Y).data), flush=True)

def memory_kb(pid):                  # Linux only: read it from /proc
    for line in open(f'/proc/{pid}/status'):
        if line.startswith('VmRSS'):
            return int(line.split()[1])

if __name__ == '__main__':
    child = multiprocessing.Process(target=last)
    child.start()
    for seconds in (5, 10, 15, 20, 25):
        time.sleep(5)
        print(f'after {seconds} s: running={child.is_alive()},',
              f'memory={memory_kb(child.pid)} kB', flush=True)
    child.kill()
