from sqlalchemy import event
from film_model import Film, engine
from pyDatalog import pyDatalog

pyDatalog.create_terms('X')

@event.listens_for(engine, 'before_cursor_execute')
def show(conn, cursor, statement, params, context, executemany):
    sql = ' '.join(statement.split())
    print('    FROM', sql.split(' FROM ')[1], params)

def titles(query):
    return sorted(row[0].title for row in query.data)

print('newer than 2000, then shorter than 100 minutes:')
for title in titles((Film.year[X] > 2000) & (Film.minutes[X] < 100)):
    print('   ', title)

print('the same, with the two conditions the other way round:')
print(len(titles((Film.minutes[X] < 100) & (Film.year[X] > 2000))), 'films')
