from model import Employee
from pyDatalog import pyDatalog

pyDatalog.create_terms('E, N, M, K, reports_to, under')

# join through the NAME column: every value stays a plain string
reports_to(N, M) <= ((Employee.name[E] == N) &
                     (Employee.manager_name[E] == M) & (M != None))
under(N, M) <= reports_to(N, M)
under(N, M) <= reports_to(N, K) & under(K, M)

print(sorted(reports_to(N, M).data))
print(sorted(under('cid', M).data))
print(sorted(under(N, 'bob').data))
