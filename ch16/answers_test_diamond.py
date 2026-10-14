from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, link, reach')

def start(*links):
    pyDatalog.clear()
    reach(X, Y) <= link(X, Y)
    reach(X, Y) <= reach(X, Z) & link(Z, Y)
    for a, b in links:
        +link(a, b)

def test_diamond():
    start(('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'd'))
    assert sorted(reach('a', Y).data) == [('b',), ('c',), ('d',)]
    assert reach('d', Y).data == []

test_diamond()
print('diamond test passed')
