from pyDatalog import pyDatalog

pyDatalog.create_terms('X, parent')

try:
    +parent('alice', X)            # a fact must be about someone
except Exception as err:
    print(type(err).__name__ + ':', err)
