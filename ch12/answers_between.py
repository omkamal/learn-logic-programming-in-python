from model import Employee
from pyDatalog import pyDatalog

pyDatalog.create_terms('X')

# at least 90 and at most 100: two conditions on the same blank
rows = (Employee.salary[X] >= 90) & (Employee.salary[X] <= 100)
print(sorted(r[0].name for r in rows.data))
