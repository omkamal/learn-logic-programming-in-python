from pyDatalog import pyDatalog

pyDatalog.create_terms('U, R, R2, P, Res, has_role, inherits, role_perm')
pyDatalog.create_terms('blocked, includes, can')

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

# an explicit block
+blocked('pat', 'write', 'report')

# a role includes the roles it inherits from (recursive literal first)
includes(R, R2) <= inherits(R, R2)
includes(R, R2) <= includes(R, P) & inherits(P, R2)

# a user can do P on Res if a role grants it and it is not blocked
can(U, P, Res) <= (has_role(U, R) & role_perm(R, P, Res)
                   & ~blocked(U, P, Res))
can(U, P, Res) <= (has_role(U, R) & includes(R, R2)
                   & role_perm(R2, P, Res) & ~blocked(U, P, Res))

for user in ['maya', 'noor', 'omar', 'pat']:
    print(user, sorted(can(user, P, 'report').data))
