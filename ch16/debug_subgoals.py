from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, C, teaches, enrolled, mentor')

+teaches('tess', 'math')
+teaches('tess', 'art')
+enrolled('ana', 'Math')                # <- a capital letter slipped in
+enrolled('ben', 'art')

mentor(X, Y) <= teaches(X, C) & enrolled(Y, C)

# we expected both ana and ben to have tess as their mentor
print(sorted(mentor(X, Y).data))

# ask the sub-goals one at a time
print(sorted(teaches('tess', C).data))   # sub-goal 1: fine
print(enrolled('ana', C).data)          # sub-goal 2: here is the bug
