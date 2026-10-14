from sqlalchemy import event
from model import Employee, engine
from pyDatalog import pyDatalog

pyDatalog.create_terms('X')

@event.listens_for(engine, 'before_cursor_execute')
def show(conn, cursor, statement, params, context, executemany):
    sql = ' '.join(statement.split())
    print('FROM', sql.split(' FROM ')[1], params)

print(sorted(r[0].name for r in (Employee.salary[X] < 90).data))
