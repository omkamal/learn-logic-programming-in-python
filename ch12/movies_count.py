from sqlalchemy import event
from film_model import Film, engine
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, T, D, M, N, Z, made, longest')

sent = []
@event.listens_for(engine, 'before_cursor_execute')
def tally(conn, cursor, statement, params, context, executemany):
    sent.append('FROM ' + ' '.join(statement.split()).split(' FROM ')[1])

# aggregates (Chapter 8) work on attributes that come from SQL rows
(made[D] == len_(T)) <= (Film.director[X] == D) & (Film.title[X] == T)
(longest[D] == max_(M, order_by=M)) <= ((Film.director[X] == D) &
                                         (Film.minutes[X] == M))

for d, n in sorted((made[D] == N).data):
    print(d, 'made', n, 'films')
print(sorted((longest[D] == Z).data))
print('statements sent:', sent)
