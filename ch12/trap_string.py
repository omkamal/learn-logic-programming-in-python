import textwrap
from model import Employee
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, above')

# recurse straight through the foreign-key column
above(X, Y) <= (Employee.manager_name[X] == Y)
above(X, Y) <= (Employee.manager_name[X] == Z) & above(Z, Y)
try:
    print(above(X, Y).data)
except AttributeError as e:
    print(textwrap.fill('AttributeError: %s' % e, 70,
                        subsequent_indent='    '))

# the same mistake, asked directly: bob is a string, not an Employee
try:
    print((Employee.manager_name['bob'] == Y).data)
except TypeError as e:
    print('TypeError:', e)
