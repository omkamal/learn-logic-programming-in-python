from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach')

def load_rules():
    reach(X, Y) <= link(X, Y)
    reach(X, Y) <= reach(X, Z) & link(Z, Y)

def start(*links):                     # a fresh, tiny world for each test
    pyDatalog.clear()
    load_rules()
    for a, b in links:
        +link(a, b)

def test_one_hop():
    start(('a', 'b'))
    assert sorted(reach('a', Y).data) == [('b',)]

def test_two_hops():
    start(('a', 'b'), ('b', 'c'))
    assert sorted(reach('a', Y).data) == [('b',), ('c',)]

def test_direction_matters():
    start(('a', 'b'))
    assert reach('b', Y).data == []    # an empty answer is an answer
    assert not bool(reach('b', 'a'))

def test_loop():
    start(('a', 'b'), ('b', 'a'))
    assert sorted(reach('a', Y).data) == [('a',), ('b',)]

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
