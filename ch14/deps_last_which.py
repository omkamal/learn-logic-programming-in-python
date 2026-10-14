# timeout: 60
import multiprocessing as mp
from pyDatalog import pyDatalog

pyDatalog.create_terms('P, Q, D, needs, requires')
for package, wanted in [
        ('shop', 'web'), ('shop', 'db'),
        ('web', 'http'), ('web', 'templates'),
        ('db', 'driver'), ('db', 'pool'),
        ('http', 'sockets'), ('http', 'tls'),
        ('templates', 'strings'), ('tls', 'crypto'),
        ('pool', 'threads'),
        ('report', 'db'), ('report', 'strings'),
        ('shop', 'auth'), ('auth', 'sessions'),
        ('sessions', 'store'), ('store', 'auth'),
        ('config', 'logging'), ('logging', 'config')]:
    +needs(package, wanted)
requires(P, D) <= needs(P, D)
requires(P, D) <= needs(P, Q) & requires(Q, D)         # recursion LAST

QUERIES = {'report needs': lambda: requires('report', D),
           'config needs': lambda: requires('config', D),
           'auth needs': lambda: requires('auth', D),
           'shop needs': lambda: requires('shop', D),
           'who needs tls': lambda: requires(P, 'tls')}

def run(case, out):
    out.put(len(QUERIES[case]().data))

if __name__ == '__main__':
    for case in QUERIES:
        queue = mp.Queue()
        child = mp.Process(target=run, args=(case, queue))
        child.start()
        child.join(5)
        if child.is_alive():
            child.kill()
            print(f'{case:14} no answer within 5 s')
        else:
            print(f'{case:14} {queue.get()} answers')
