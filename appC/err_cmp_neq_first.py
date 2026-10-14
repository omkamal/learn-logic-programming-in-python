from pyDatalog import pyDatalog

pyDatalog.create_terms('P, X, Y, parent, sibling, twin')
+parent('alice', 'bob')
+parent('alice', 'carol')

# the inequality first, and in the middle (brackets are there)
sibling(X, Y) <= (X != Y) & parent(P, X) & parent(P, Y)
twin(X, Y) <= parent(P, X) & (X != Y) & parent(P, Y)
for rule in (sibling, twin):
    try:
        print(rule(X, Y))
    except Exception as err:
        print(type(err).__name__ + ':', err)
