from pyDatalog import pyDatalog

pyDatalog.create_terms('parent')

try:
    +parent(alice, bob)
except NameError as err:
    print('NameError:', err)
