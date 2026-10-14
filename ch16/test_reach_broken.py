from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach')

def load_rules():
    reach(X, Y) <= link(X, Y)          # the recursive clause is missing

def start(*links):
    pyDatalog.clear()
    load_rules()
    for a, b in links:
        +link(a, b)

def test_one_hop():
    start(('a', 'b'))
    assert sorted(reach('a', Y).data) == [('b',)]

def test_two_hops():
    start(('a', 'b'), ('b', 'c'))
    answers = sorted(reach('a', Y).data)
    assert answers == [('b',), ('c',)], 'got %s' % answers

def run_all():
    for name, test in sorted(globals().items()):
        if name.startswith('test_'):
            try:
                test()
                print('PASS', name)
            except AssertionError as failure:
                print('FAIL', name, failure)

if __name__ == '__main__':
    run_all()
