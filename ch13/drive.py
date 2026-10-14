from pyDatalog import pyDatalog

pyDatalog.create_terms('U, P, F, A, B, folder_in, inside, grant, lock')
pyDatalog.create_terms('holds, shut, can')

# the folder tree: folder_in(child, parent)
for child, parent in [('finance', 'drive'), ('marketing', 'drive'),
                      ('budgets', 'finance'), ('taxes', 'finance'),
                      ('q1', 'budgets'), ('campaigns', 'marketing')]:
    +folder_in(child, parent)

# grants: a person may do something in a folder and everything below it
+grant('sam', 'edit', 'finance')
+grant('sam', 'view', 'drive')
+grant('tia', 'view', 'drive')
+grant('uma', 'edit', 'marketing')

# a lock shuts one person out of a folder and everything below it
+lock('sam', 'taxes')

# F is inside A: a folder at any depth below A
inside(F, A) <= folder_in(F, A)
inside(F, A) <= inside(F, B) & folder_in(B, A)

# a grant on F itself, or on any folder that F is inside
holds(U, P, F) <= grant(U, P, F)
holds(U, P, F) <= inside(F, A) & grant(U, P, A)

# a lock on F itself, or on any folder that F is inside
shut(U, F) <= lock(U, F)
shut(U, F) <= inside(F, A) & lock(U, A)

# allowed = granted and not shut out (the not comes last)
can(U, P, F) <= holds(U, P, F) & ~shut(U, F)

def names(query):
    return sorted(row[0] for row in query.data)

print('q1 is inside:      ', *names(inside('q1', A)))
print('sam can edit in:   ', *names(can('sam', 'edit', F)))
print('sam can view in:   ', *names(can('sam', 'view', F)))
print('who can view q1:   ', *names(can(U, 'view', 'q1')))
print('who can edit taxes:', names(can(U, 'edit', 'taxes')))
print('sam on taxes:      ', sorted(can('sam', P, 'taxes').data))
