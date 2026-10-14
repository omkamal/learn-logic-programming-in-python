from pyDatalog import pyDatalog

pyDatalog.create_terms('parent')

try:
    +parent(alice, 'bob')          # alice has no quotes
except Exception as err:
    print(type(err).__name__ + ':', err)
