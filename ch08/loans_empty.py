from pyDatalog import pyDatalog

pyDatalog.create_terms('M, B, Z, member, loan, loans, idle, busy')

for who in ['mia', 'noor', 'omar', 'pat']:
    +member(who)
for who, book in [('mia', 'atlas'), ('mia', 'birds'), ('mia', 'comets'),
                  ('noor', 'atlas'), ('pat', 'birds'), ('pat', 'comets')]:
    +loan(who, book)

(loans[M] == len_(B)) <= loan(M, B)
idle(M) <= member(M) & ~loan(M, B)        # negation: bind M first
busy(M) <= (loans[M] == Z) & (Z > 2)      # a gate on the aggregate

print(sorted((loans['omar'] == Z).data))  # an empty basket: no row
print(sorted(idle(M).data))
print(sorted(busy(M).data))
