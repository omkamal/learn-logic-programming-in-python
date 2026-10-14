from pyDatalog import pyDatalog

pyDatalog.create_terms('S, A, student, assignment, submitted, missing')
for s in ['ada', 'ben', 'chen', 'dina', 'eli']:
    +student(s)
for a in ['a1', 'a2']:
    +assignment(a)
for s, a in [('ada', 'a1'), ('ada', 'a2'), ('ben', 'a1'),
             ('chen', 'a1'), ('chen', 'a2'), ('eli', 'a2')]:
    +submitted(s, a)
missing(S, A) <= student(S) & assignment(A) & ~submitted(S, A)

+submitted('dina', 'a1')               # dina hands in a1 late
print(sorted(missing(S, A).data))
+assignment('a3')                      # a new assignment is announced
print(len(missing(S, A).data), 'pairs missing')
print(sorted(missing('frank', A).data))    # frank is not on the roster
