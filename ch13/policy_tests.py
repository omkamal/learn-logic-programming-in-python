from pyDatalog import pyDatalog

pyDatalog.create_terms('U, R, R2, P, Res, has_role, inherits, role_perm')
pyDatalog.create_terms('blocked, includes, can, loop_role')

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
loop_role(R) <= includes(R, R)

# 1. the expected answers, written down by hand BEFORE running anything
expected = {('maya', 'read'), ('maya', 'write'), ('maya', 'delete'),
            ('noor', 'read'), ('noor', 'write'), ('omar', 'read'),
            ('pat', 'read')}
actual = set(can(U, P, 'report').data)
assert actual == expected, actual ^ expected

# 2. rules that must hold whatever the data is
assert not loop_role(R).data, 'a role includes itself'
for user, perm, res in blocked(U, P, Res).data:
    assert not can(user, perm, res), (user, perm, res)

# 3. one test per block: lifting it must change exactly one answer
-blocked('pat', 'write', 'report')
assert set(can(U, P, 'report').data) - actual == {('pat', 'write')}
+blocked('pat', 'write', 'report')

print('all checks passed:', len(expected), 'answers, 0 loops, 1 block')
