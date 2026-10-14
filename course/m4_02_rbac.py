from pyDatalog import pyDatalog

pyDatalog.create_terms('U, R, R2, P, Res, has_role, inherits, role_perm, can, denied, blocked')

# who has which role
+has_role('maya', 'admin')
+has_role('noor', 'editor')
+has_role('omar', 'viewer')
+has_role('pat',  'editor')

# role inheritance: admin > editor > viewer
+inherits('admin', 'editor')
+inherits('editor', 'viewer')

# permissions granted to a role directly
+role_perm('viewer', 'read', 'report')
+role_perm('editor', 'write', 'report')
+role_perm('admin',  'delete', 'report')

# explicit blocks
+blocked('pat', 'write', 'report')

# a role includes the roles it inherits from (recursive, recursive literal first)
pyDatalog.create_terms('includes')
includes(R, R2) <= inherits(R, R2)
includes(R, R2) <= includes(R, P) & inherits(P, R2)

# a user can do P on Res if one of their roles (or an inherited role) grants it, and it isn't blocked
can(U, P, Res) <= has_role(U, R) & role_perm(R, P, Res) & ~blocked(U, P, Res)
can(U, P, Res) <= has_role(U, R) & includes(R, R2) & role_perm(R2, P, Res) & ~blocked(U, P, Res)

for user in ['maya', 'noor', 'omar', 'pat']:
    print(user, sorted(can(user, P, 'report').data))
