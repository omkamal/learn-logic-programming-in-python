from pyDatalog import pyDatalog

pyDatalog.create_terms('R, S, P, inherits, includes')
for a, b in [('admin', 'editor'), ('editor', 'viewer'),
             ('viewer', 'admin')]:               # a loop of three roles
    +inherits(a, b)

includes(R, S) <= inherits(R, S)
includes(R, S) <= includes(R, P) & inherits(P, S)    # recursion first
print(len(includes(R, S).data), 'pairs: every role includes every role')
print(sorted(includes(R, R).data))                   # the alarm
