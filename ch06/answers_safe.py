from pyDatalog import pyDatalog

pyDatalog.create_terms('S, A, student, submitted, v1, v2, v3')
for s in ['ada', 'ben', 'chen']:
    +student(s)
for s in ['ada', 'chen']:
    +submitted(s)

v1(S) <= ~submitted(S) & student(S)      # not first
v2(S) <= student(S) & ~submitted(S)      # fill first
v3(S) <= student(S) & ~submitted(A)      # the blank A is private

print(sorted(v1(S).data))
print(sorted(v2(S).data))
print(sorted(v3(S).data))
