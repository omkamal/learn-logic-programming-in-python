from pyDatalog import pyDatalog

pyDatalog.create_terms('U, R, R2, P, Res, has_role, inherits, role_perm')
pyDatalog.create_terms('blocked, includes, can')

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

# the whole policy in one question: any user, any permission
rows = sorted(can(U, P, 'report').data)
print(len(rows), 'rows')
for user, perm in rows:
    print(f'{user:5} {perm}')

# yes/no questions: a query with no blanks
print('may omar delete?', bool(can('omar', 'delete', 'report')))
print('may pat write?  ', bool(can('pat', 'write', 'report')))
print('may pat read?   ', bool(can('pat', 'read', 'report')))
print('may zed read?   ', bool(can('zed', 'read', 'report')))
