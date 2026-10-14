from pyDatalog import pyDatalog

pyDatalog.create_terms('X, parent, sibling, empty')
+parent('alice', 'bob')
parent('carol', 'dan')             # no plus sign: only a question
print(sorted(parent(X, 'dan').data))

# a name that was created but never given a fact or a rule in its body
sibling(X, 'bob') <= empty(X)
print(sorted(sibling(X, 'bob').data))
