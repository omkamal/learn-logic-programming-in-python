from pprint import pprint
from pyDatalog import pyDatalog

pyDatalog.create_terms('M, B, Z, member, loan, loans, titles, shelf, idle')

for who in ['mia', 'noor', 'omar', 'pat']:
    +member(who)
for who, book in [('mia', 'atlas'), ('mia', 'birds'), ('mia', 'comets'),
                  ('noor', 'atlas'), ('pat', 'birds'), ('pat', 'comets')]:
    +loan(who, book)

(loans[M]  == len_(B))                         <= loan(M, B)
(titles[M] == concat_(B, order_by=B, sep=', ')) <= loan(M, B)
(shelf[M]  == tuple_(B, order_by=B))           <= loan(M, B)

print(sorted((loans[M] == Z).data))
print(sorted((titles[M] == Z).data))
pprint(sorted((shelf[M] == Z).data), width=70)
