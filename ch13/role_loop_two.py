# timeout: 10
from pyDatalog import pyDatalog

pyDatalog.create_terms('R, R2, P, inherits, includes')

+inherits('editor', 'viewer')
+inherits('viewer', 'editor')       # a loop of only two roles

includes(R, R2) <= inherits(R, R2)
includes(R, R2) <= inherits(R, P) & includes(P, R2)   # recursion last

print(*[f'{a}>{b}' for a, b in sorted(includes(R, R2).data)])
