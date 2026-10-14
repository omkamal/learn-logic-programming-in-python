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

def names(query):
    return sorted(row[0] for row in query.data)

print(*names(prereq('learning', P)))
print(*names(prereq('algorithms', P)))
print(*names(prereq(C, 'programming')))
