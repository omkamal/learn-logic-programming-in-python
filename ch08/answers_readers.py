from pyDatalog import pyDatalog

pyDatalog.create_terms('M, B, Z, loan, readers')
for who, book in [('mia', 'atlas'), ('mia', 'birds'), ('mia', 'comets'),
                  ('noor', 'atlas'), ('pat', 'birds'), ('pat', 'comets')]:
    +loan(who, book)

(readers[B] == concat_(M, order_by=M, sep='/')) <= loan(M, B)
print(sorted((readers[B] == Z).data))
