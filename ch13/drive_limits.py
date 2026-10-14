from pyDatalog import pyDatalog

pyDatalog.create_terms('U, P, F, A, B, folder_in, inside, grant, lock')
pyDatalog.create_terms('holds, shut, can')

for child, parent in [('finance', 'drive'), ('marketing', 'drive'),
                      ('budgets', 'finance'), ('taxes', 'finance'),
                      ('q1', 'budgets'), ('campaigns', 'marketing')]:
    +folder_in(child, parent)
+grant('sam', 'edit', 'finance')
+grant('sam', 'view', 'drive')
+lock('sam', 'finance')            # lock the whole finance branch
+grant('sam', 'edit', 'q1')        # ...and grant one folder inside it

inside(F, A) <= folder_in(F, A)
inside(F, A) <= inside(F, B) & folder_in(B, A)
holds(U, P, F) <= grant(U, P, F)
holds(U, P, F) <= inside(F, A) & grant(U, P, A)
shut(U, F) <= lock(U, F)
shut(U, F) <= inside(F, A) & lock(U, A)
can(U, P, F) <= holds(U, P, F) & ~shut(U, F)

def names(query):
    return sorted(row[0] for row in query.data)

print('sam can edit in:', names(can('sam', 'edit', F)))
print('sam can view in:', *names(can('sam', 'view', F)))
print('granted on q1?  ', bool(holds('sam', 'edit', 'q1')))
print('allowed on q1?  ', bool(can('sam', 'edit', 'q1')))
