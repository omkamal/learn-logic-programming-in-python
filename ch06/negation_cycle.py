# timeout: 60
import multiprocessing
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, a, b, p, city')

def run_job(job, box):                # this runs inside the new process
    try:
        box.put(('answer', job()))
    except Exception as err:
        box.put(('error', type(err).__name__))

def with_timeout(job, seconds):
    box = multiprocessing.Queue()
    child = multiprocessing.Process(target=run_job, args=(job, box))
    child.start()
    child.join(seconds)
    if child.is_alive():              # no answer in time: stop it
        child.kill()
        child.join()
        return ('timeout', None)
    return box.get()

def two_rules():                      # a is "not b" and b is "not a"
    +city('x')
    a(X) <= city(X) & ~b(X)
    b(X) <= city(X) & ~a(X)
    return sorted(a(X).data)

def one_rule():                       # p is "not p"
    +city('x')
    p(X) <= city(X) & ~p(X)
    return sorted(p(X).data)

if __name__ == '__main__':
    for name, job in [('two rules that negate each other', two_rules),
                      ('one rule that negates itself', one_rule)]:
        status, value = with_timeout(job, 5)
        print(name + ':', value if value else 'no answer in 5 s')
