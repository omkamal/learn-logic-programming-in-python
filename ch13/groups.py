from pyDatalog import pyDatalog

pyDatalog.create_terms('U, G, H, R, R2, P, Res, has_role, group_role')
pyDatalog.create_terms('member_of, group_in, in_group, holds_role')
pyDatalog.create_terms('inherits, role_perm, blocked, includes, can')

# people belong to groups; groups belong to bigger groups
for person, group in [('ivan', 'interns'), ('cora', 'interns'),
                      ('cora', 'contractors'), ('lena', 'leads')]:
    +member_of(person, group)
for small, big in [('interns', 'staff'), ('leads', 'staff'),
                   ('staff', 'everyone'), ('contractors', 'everyone')]:
    +group_in(small, big)
# roles can be given to a whole group
+group_role('everyone', 'viewer')
+group_role('leads', 'editor')
+has_role('maya', 'admin')

# U is in G directly, or in a group that is inside G (recursive first)
in_group(U, G) <= member_of(U, G)
in_group(U, G) <= in_group(U, H) & group_in(H, G)

# a person holds a role they were given, or a role of one of their groups
holds_role(U, R) <= has_role(U, R)
holds_role(U, R) <= in_group(U, G) & group_role(G, R)

# the role chart and the permissions are as before
+inherits('admin', 'editor')
+inherits('editor', 'viewer')
for role, perm in [('viewer', 'read'), ('editor', 'write'),
                   ('admin', 'delete')]:
    +role_perm(role, perm, 'report')
+blocked('pat', 'write', 'report')
includes(R, R2) <= inherits(R, R2)
includes(R, R2) <= includes(R, P) & inherits(P, R2)
can(U, P, Res) <= (holds_role(U, R) & role_perm(R, P, Res)
                   & ~blocked(U, P, Res))
can(U, P, Res) <= (holds_role(U, R) & includes(R, R2)
                   & role_perm(R2, P, Res) & ~blocked(U, P, Res))

def names(query):
    return sorted(row[0] for row in query.data)

print('cora is in:', *names(in_group('cora', G)))
for user in ['ivan', 'cora', 'lena', 'maya']:
    print(f'{user:5}', 'roles:', names(holds_role(user, R)),
          ' may:', names(can(user, P, 'report')))

# a slip: the biggest group is put inside the smallest one
+group_in('everyone', 'interns')
print('after the slip, ivan is in:', *names(in_group('ivan', G)))
