from model import Employee
from pyDatalog import pyDatalog

pyDatalog.create_terms('E, M, boss_bad, boss_ok')

boss_bad(M) <= (Employee.manager_name[E] == M)
boss_ok(M) <= (Employee.manager_name[E] == M) & (M != None)

print(sorted(boss_bad(M).data, key=str))
print(sorted(boss_ok(M).data))
