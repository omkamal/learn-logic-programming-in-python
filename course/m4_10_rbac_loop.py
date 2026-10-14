from pyDatalog import pyDatalog

pyDatalog.create_terms('U, R, R2, P, Res, has_role, inherits, role_perm, can, denied, blocked')

# the same facts and rules as m4_02_rbac.py ...
+has_role('maya', 'admin')
+has_role('noor', 'editor')
+has_role('omar', 'viewer')
+has_role('pat',  'editor')

+inherits('admin', 'editor')
+inherits('editor', 'viewer')

+role_perm('viewer', 'read', 'report')
+role_perm('editor', 'write', 'report')
+role_perm('admin',  'delete', 'report')

+blocked('pat', 'write', 'report')

# ... plus ONE accidental fact that closes a loop: admin > editor > viewer > admin
+inherits('viewer', 'admin')

pyDatalog.create_terms('includes')
includes(R, R2) <= inherits(R, R2)
includes(R, R2) <= includes(R, P) & inherits(P, R2)   # recursive literal first

can(U, P, Res) <= has_role(U, R) & role_perm(R, P, Res) & ~blocked(U, P, Res)
can(U, P, Res) <= has_role(U, R) & includes(R, R2) & role_perm(R2, P, Res) & ~blocked(U, P, Res)

# the query still finishes, but the loop makes every role include every other role
for user in ['maya', 'noor', 'omar', 'pat']:
    print(user, sorted(can(user, P, 'report').data))
