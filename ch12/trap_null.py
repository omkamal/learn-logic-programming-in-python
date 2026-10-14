from sqlalchemy import event
from model import Employee, engine
from pyDatalog import pyDatalog

pyDatalog.create_terms('E, N, M, K, raw_reports, raw_under')

@event.listens_for(engine, 'before_cursor_execute')
def show(conn, cursor, statement, params, context, executemany):
    sql = ' '.join(statement.split())
    print('    FROM', sql.split(' FROM ')[1], params)

# the name join WITHOUT the (M != None) filter
raw_reports(N, M) <= ((Employee.name[E] == N) &
                      (Employee.manager_name[E] == M))
raw_under(N, M) <= raw_reports(N, M)
raw_under(N, M) <= raw_reports(N, K) & raw_under(K, M)

print('above cid:')
print(sorted(raw_under('cid', M).data, key=str))
print('every pair:')
print(sorted(raw_reports(N, M).data, key=str))
