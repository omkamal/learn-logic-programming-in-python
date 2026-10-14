from sqlalchemy import event, text
from model import Employee, engine, session
from pyDatalog import pyDatalog

pyDatalog.create_terms('E, N, M, K, reports_to, under')
reports_to(N, M) <= ((Employee.name[E] == N) &
                     (Employee.manager_name[E] == M) & (M != None))
under(N, M) <= reports_to(N, M)
under(N, M) <= reports_to(N, K) & under(K, M)

count = []
@event.listens_for(engine, 'before_cursor_execute')
def tally(conn, cursor, statement, params, context, executemany):
    count.append(statement)

print(sorted(under('cid', M).data))
print('statements sent by the rules:', len(count))

count.clear()
rows = session.execute(text("""
    WITH RECURSIVE above(name) AS (
        SELECT manager_name FROM employee WHERE name = 'cid'
        UNION
        SELECT e.manager_name FROM employee e JOIN above a
            ON e.name = a.name
    )
    SELECT name FROM above WHERE name IS NOT NULL ORDER BY name"""))
print(rows.fetchall())
print('statements sent by the CTE:', len(count))
