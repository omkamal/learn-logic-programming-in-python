from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, parent')

try:
    nanny(X, Y) <= parent(X, Y)    # nanny was never created
except Exception as err:
    print(type(err).__name__ + ':', err)
