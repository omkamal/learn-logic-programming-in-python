from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, C, line, ride')

# a one-way toy metro: a main line and a branch to the stadium
for a, b in [('oldtown', 'market'), ('market', 'harbor'),
             ('harbor', 'airport'), ('market', 'stadium')]:
    +line(a, b)

ride(A, B) <= line(A, B)
ride(A, B) <= ride(A, C) & line(C, B)

print(sorted(ride('oldtown', B).data))
print(sorted(ride(A, 'airport').data))
print(bool(ride('stadium', 'airport')))
