from pyDatalog import pyDatalog

pyDatalog.create_terms('R, R2, P, inherits, includes')

+inherits('admin', 'editor')
+inherits('editor', 'viewer')

includes(R, R2) <= inherits(R, R2)
includes(R, R2) <= includes(R, P) & inherits(P, R2)

print('written down:', sorted(inherits(R, R2).data))
print('worked out:  ', sorted(includes(R, R2).data))
print('admin includes', sorted(includes('admin', R2).data))
print('admin inherits from viewer?', bool(inherits('admin', 'viewer')))
print('admin includes viewer?     ', bool(includes('admin', 'viewer')))
