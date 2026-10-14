from pyDatalog import pyDatalog
from pyDatalog.util import DatalogError

pyDatalog.create_terms('X, parent')

try:
    +parent('alice', X)
except DatalogError as err:
    print('DatalogError:', err)
