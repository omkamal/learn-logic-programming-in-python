from pyDatalog import pyDatalog

pyDatalog.create_terms('S, A, student, assignment, submitted, missing')
for s in ['ada', 'ben', 'chen', 'dina', 'eli']:
    +student(s)
for a in ['a1', 'a2']:
    +assignment(a)
for s, a in [('ada', 'a1'), ('ada', 'a2'), ('ben', 'a1'),
             ('chen', 'a1'), ('chen', 'a2'), ('eli', 'a2')]:
    +submitted(s, a)

# fill S and A first, then ask the ~ about that pair
missing(S, A) <= student(S) & assignment(A) & ~submitted(S, A)

print(sorted(missing(S, A).data))
print(sorted(missing('dina', A).data))
