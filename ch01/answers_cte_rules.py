# Answer to exercise 3: the company query as two rules.
from pyDatalog import pyDatalog

pyDatalog.create_terms('reports_to, above, X, Y, Z')

+reports_to('bob', 'ann')       # ann has no manager, so no fact for ann
+reports_to('cid', 'bob')
+reports_to('dee', 'bob')

above(X, Y) <= reports_to(X, Y)                       # the base case
above(X, Y) <= above(X, Z) & reports_to(Z, Y)         # one more step up

print(sorted(above('cid', Y).data))
