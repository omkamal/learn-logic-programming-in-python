from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, C, D, enrolled, classmate')
for name, course in [('ana', 'math'), ('ben', 'math'), ('cy', 'math'),
                     ('dee', 'art'), ('eli', 'art'), ('fay', 'art')]:
    +enrolled(name, course)

# a typo: D appears nowhere else in the body, so it ties nothing
classmate(X, Y) <= enrolled(X, C) & enrolled(Y, D) & (X != Y)
print(len(classmate(X, Y).data), 'pairs, 12 expected')
print(('ana', 'dee') in classmate(X, Y).data)
