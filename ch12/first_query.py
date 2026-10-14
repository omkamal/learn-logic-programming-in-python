from model import Employee
from pyDatalog import pyDatalog

pyDatalog.create_terms('X')

rows = (Employee.salary[X] > 85).data       # one blank, one condition
print(sorted(rows, key=lambda r: r[0].name))
print(type(rows[0][0]).__name__)
