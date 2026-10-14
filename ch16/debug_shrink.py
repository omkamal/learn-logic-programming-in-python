from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, C, D, enrolled, classmate')

# the rule has a typo: D where C was meant
classmate(X, Y) <= enrolled(X, C) & enrolled(Y, D) & (X != Y)

# 1. the real data: six students in two classes
for name, course in [('ana', 'math'), ('ben', 'math'), ('cy', 'math'),
                     ('dee', 'art'), ('eli', 'art'), ('fay', 'art')]:
    +enrolled(name, course)
print(len(classmate(X, Y).data), 'classmate pairs (expected 12)')

# 2. shrink: two students in two different classes
pyDatalog.clear()
classmate(X, Y) <= enrolled(X, C) & enrolled(Y, D) & (X != Y)
+enrolled('ana', 'math')
+enrolled('dee', 'art')
print(sorted(classmate(X, Y).data))     # they are not classmates!
