from sqlalchemy import event
from model import Employee, engine
from pyDatalog import pyDatalog

pyDatalog.create_terms('X')

@event.listens_for(engine, 'before_cursor_execute')
def show(conn, cursor, statement, params, context, executemany):
    lines = statement.replace(', ', ',\n       ').splitlines()
    print('\n'.join(line.rstrip() for line in lines))
    print('parameters:', params)

rows = (Employee.salary[X] > 85).data
print(sorted(r[0].name for r in rows))
