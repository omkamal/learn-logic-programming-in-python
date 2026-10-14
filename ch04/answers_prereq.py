from pyDatalog import pyDatalog

pyDatalog.create_terms('C, P, Q, needs, prereq')

for course, before in [('structures', 'programming'),
                       ('discrete', 'programming'),
                       ('algorithms', 'structures'),
                       ('algorithms', 'discrete'),
                       ('databases', 'structures'),
                       ('learning', 'algorithms'),
                       ('learning', 'statistics')]:
    +needs(course, before)

prereq(C, P) <= needs(C, P)
prereq(C, P) <= prereq(C, Q) & needs(Q, P)

print(sorted(prereq('databases', P).data))
print(len(prereq('learning', P).data), 'rows for learning')
