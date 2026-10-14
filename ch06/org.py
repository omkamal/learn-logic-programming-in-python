from pyDatalog import pyDatalog

pyDatalog.create_terms('E, M, X, employee, reports_to, root, leaf')
for e in ['ivy', 'jon', 'kim', 'lee', 'max', 'ned']:
    +employee(e)
for e, m in [('jon', 'ivy'), ('kim', 'ivy'), ('lee', 'jon'),
             ('max', 'jon'), ('ned', 'kim')]:
    +reports_to(e, m)

root(E) <= employee(E) & ~reports_to(E, M)   # has no manager at all
leaf(E) <= employee(E) & ~reports_to(X, E)   # nobody reports to E

print(sorted(root(E).data))
print(sorted(leaf(E).data))
