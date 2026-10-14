from pyDatalog import pyDatalog

pyDatalog.create_terms('U, R, R2, P, Res, has_role, inherits, role_perm')
pyDatalog.create_terms('blocked, includes, can, can_early')

for user, role in [('maya', 'admin'), ('noor', 'editor'),
                   ('omar', 'viewer'), ('pat', 'editor')]:
    +has_role(user, role)
+inherits('admin', 'editor')
+inherits('editor', 'viewer')
for role, perm in [('viewer', 'read'), ('editor', 'write'),
                   ('admin', 'delete')]:
    +role_perm(role, perm, 'report')
+blocked('pat', 'write', 'report')

includes(R, R2) <= inherits(R, R2)
includes(R, R2) <= includes(R, P) & inherits(P, R2)

# the check "not blocked" written FIRST in both clauses
can_early(U, P, Res) <= (~blocked(U, P, Res) & has_role(U, R)
                         & role_perm(R, P, Res))
can_early(U, P, Res) <= (~blocked(U, P, Res) & has_role(U, R)
                         & includes(R, R2) & role_perm(R2, P, Res))

print('who can do what:', sorted(can_early(U, P, 'report').data))
print('may pat read?   ', bool(can_early('pat', 'read', 'report')))
print('may pat write?  ', bool(can_early('pat', 'write', 'report')))
print('what can noor do?', sorted(can_early('noor', P, 'report').data))
print('what can pat do?', sorted(can_early('pat', P, 'report').data))

# lift the only block: the broken rule suddenly "works"
-blocked('pat', 'write', 'report')
rows = sorted(can_early(U, P, 'report').data)
print('after the retract:', len(rows), 'rows')
print('pat:', [p for u, p in rows if u == 'pat'])
