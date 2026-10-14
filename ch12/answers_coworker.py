from model import Employee
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, A, B, M, coworker')

# two different employees with the same manager
coworker(A, B) <= ((Employee.name[X] == A) &
                   (Employee.manager_name[X] == M) & (M != None) &
                   (Employee.name[Y] == B) &
                   (Employee.manager_name[Y] == M) & (A != B))
print(sorted(coworker(A, B).data))
