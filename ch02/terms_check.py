# Capitalized names become variables; lowercase names do not
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, x, parent')
print('X is a variable:', X.is_variable())
print('Y is a variable:', Y.is_variable())
print('x is a variable:', x.is_variable())
print('parent(...) builds a', type(parent('alice', X)).__name__)
