from pyDatalog import pyDatalog

pyDatalog.create_terms('U, P, F, A, B, folder_in, inside, grant, lock')
pyDatalog.create_terms('holds, shut, can')

for child, parent in [('finance', 'drive'), ('marketing', 'drive'),
                      ('budgets', 'finance'), ('taxes', 'finance'),
                      ('q1', 'budgets'), ('campaigns', 'marketing')]:
    +folder_in(child, parent)
+grant('sam', 'edit', 'finance')
+grant('sam', 'view', 'drive')
+grant('tia', 'view', 'drive')
+grant('uma', 'edit', 'marketing')
+lock('sam', 'taxes')

inside(F, A) <= folder_in(F, A)
inside(F, A) <= inside(F, B) & folder_in(B, A)
holds(U, P, F) <= grant(U, P, F)
holds(U, P, F) <= inside(F, A) & grant(U, P, A)
shut(U, F) <= lock(U, F)
shut(U, F) <= inside(F, A) & lock(U, A)
can(U, P, F) <= holds(U, P, F) & ~shut(U, F)

+grant('tia', 'edit', 'budgets')     # the new grant
+lock('tia', 'q1')                   # the new lock

def names(query):
    return sorted(row[0] for row in query.data)

print('tia can edit in:', names(can('tia', 'edit', F)))
print('tia can view in:', names(can('tia', 'view', F)))
