from pyDatalog import pyDatalog


def declare():
    pyDatalog.create_terms('X, parent')


declare()
try:
    +parent('alice', 'bob')        # the names did not reach this level
except Exception as err:
    print(type(err).__name__ + ':', err)
