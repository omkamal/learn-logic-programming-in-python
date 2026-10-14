from pyDatalog import pyDatalog

pyDatalog.create_terms('X, p, q')
+q(1)

p(X) <= q(X) & ~p(X)               # p holds exactly when it does not
print(sorted(p(X).data))
print(bool(p(1)))
