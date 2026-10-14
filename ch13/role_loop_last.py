# timeout: 10
from pyDatalog import pyDatalog

pyDatalog.create_terms('U, R, R2, P, Res, has_role, inherits, role_perm')
pyDatalog.create_terms('blocked, includes, can, loop_role')

for user, role in [('maya', 'admin'), ('noor', 'editor'),
                   ('omar', 'viewer'), ('pat', 'editor')]:
    +has_role(user, role)
+inherits('admin', 'editor')
+inherits('editor', 'viewer')
+inherits('viewer', 'admin')       # the slip: a loop in the role chart
for role, perm in [('viewer', 'read'), ('editor', 'write'),
                   ('admin', 'delete')]:
    +role_perm(role, perm, 'report')
+blocked('pat', 'write', 'report')

includes(R, R2) <= inherits(R, R2)
includes(R, R2) <= inherits(R, P) & includes(P, R2)

can(U, P, Res) <= (has_role(U, R) & role_perm(R, P, Res)
                   & ~blocked(U, P, Res))
can(U, P, Res) <= (has_role(U, R) & includes(R, R2)
                   & role_perm(R2, P, Res) & ~blocked(U, P, Res))

for user in ['maya', 'noor', 'omar', 'pat']:
    print(user, sorted(can(user, P, 'report').data))

# a guard: no role should include itself
loop_role(R) <= includes(R, R)
print('roles in a loop:', sorted(loop_role(R).data))
