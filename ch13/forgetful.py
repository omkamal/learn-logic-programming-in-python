from pyDatalog import pyDatalog

pyDatalog.create_terms('U, R, R2, P, Res, has_role, inherits, role_perm')
pyDatalog.create_terms('blocked, includes, can, can_forgetful')

for user, role in [('maya', 'admin'), ('noor', 'editor'),
                   ('omar', 'viewer'), ('pat', 'editor')]:
    +has_role(user, role)
+inherits('admin', 'editor')
+inherits('editor', 'viewer')
for role, perm in [('viewer', 'read'), ('editor', 'write'),
                   ('admin', 'delete')]:
    +role_perm(role, perm, 'report')
+blocked('pat', 'write', 'report')
+blocked('maya', 'write', 'report')    # maya is on leave

includes(R, R2) <= inherits(R, R2)
includes(R, R2) <= includes(R, P) & inherits(P, R2)

# the real policy: both clauses end with "and not blocked"
can(U, P, Res) <= (has_role(U, R) & role_perm(R, P, Res)
                   & ~blocked(U, P, Res))
can(U, P, Res) <= (has_role(U, R) & includes(R, R2)
                   & role_perm(R2, P, Res) & ~blocked(U, P, Res))

# a slip: the second clause forgets the check
can_forgetful(U, P, Res) <= (has_role(U, R) & role_perm(R, P, Res)
                             & ~blocked(U, P, Res))
can_forgetful(U, P, Res) <= (has_role(U, R) & includes(R, R2)
                             & role_perm(R2, P, Res))

for user in ['maya', 'pat']:
    print(f'{user:5} real:     ', sorted(can(user, P, 'report').data))
    print(f'{user:5} forgetful:',
          sorted(can_forgetful(user, P, 'report').data))
