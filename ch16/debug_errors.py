from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent')
+parent('alice', 'bob')
+parent('bob', 'carol')

# 1. a fact with the wrong number of arguments
try:
    print(parent('alice', 'bob', 'x').data)
except Exception as error:
    print(type(error).__name__ + ':', error)

# 2. a name that was never declared with create_terms
try:
    nanny(X) <= parent(X, Y)
except Exception as error:
    print(type(error).__name__ + ':', error)

# 3. the right question with the wrong capital letter: no error at all
print(parent('Alice', Y).data)
