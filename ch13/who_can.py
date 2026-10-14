from pyDatalog import pyDatalog

pyDatalog.create_terms('U, R, R2, P, Res, has_role, inherits, role_perm')
pyDatalog.create_terms('blocked, includes, can')

# the same facts and rules as policy.py
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
can(U, P, Res) <= (has_role(U, R) & role_perm(R, P, Res)
                   & ~blocked(U, P, Res))
can(U, P, Res) <= (has_role(U, R) & includes(R, R2)
                   & role_perm(R2, P, Res) & ~blocked(U, P, Res))

# the opening question, asked the other way round
print('delete:', sorted(can(U, 'delete', 'report').data))
print('write: ', sorted(can(U, 'write', 'report').data))

# lifting pat's block is one retracted fact
-blocked('pat', 'write', 'report')
print('write: ', sorted(can(U, 'write', 'report').data))

# and putting it back is one asserted fact
+blocked('pat', 'write', 'report')
print('write: ', sorted(can(U, 'write', 'report').data))
