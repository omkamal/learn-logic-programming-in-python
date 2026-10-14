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
+blocked('maya', 'write', 'report')
includes(R, R2) <= inherits(R, R2)
includes(R, R2) <= includes(R, P) & inherits(P, R2)

# the forgetful policy of the chapter: no check in the second clause
can_forgetful(U, P, Res) <= (has_role(U, R) & role_perm(R, P, Res)
                             & ~blocked(U, P, Res))
can_forgetful(U, P, Res) <= (has_role(U, R) & includes(R, R2)
                             & role_perm(R2, P, Res))

# the invariant of policy_tests.py: nobody blocked can do the blocked thing
for user, perm, res in sorted(blocked(U, P, Res).data):
    try:
        assert not can_forgetful(user, perm, res), (user, perm, res)
        print('ok:    ', user, perm, res)
    except AssertionError as error:
        print('caught:', error)
