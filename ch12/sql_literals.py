from sqlalchemy import event
from model import Employee, engine
from pyDatalog import pyDatalog

pyDatalog.create_terms('X')

@event.listens_for(engine, 'before_cursor_execute')
def show(conn, cursor, statement, params, context, executemany):
    rest = ' '.join(statement.split()).split(' FROM ')[1]
    print('    FROM', rest, params)

def ask(label, query):
    print(label)
    print('   ', sorted(r[0].name for r in query.data))

ask('salary > 85', Employee.salary[X] > 85)
ask('salary == 100', Employee.salary[X] == 100)
ask('90 <= salary < 150',
    (Employee.salary[X] >= 90) & (Employee.salary[X] < 150))
