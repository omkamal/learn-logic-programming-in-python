from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, D, P, works_in, on_project, colleague, '
                       'teammate, can_ask')

+works_in('ann', 'eng')
+works_in('bob', 'eng')
+works_in('cid', 'ops')
+works_in('dee', 'ops')
+works_in('eli', 'hr')

+on_project('ann', 'billing')
+on_project('cid', 'billing')
+on_project('eli', 'billing')
+on_project('bob', 'mobile')
+on_project('dee', 'mobile')

colleague(A, B) <= works_in(A, D) & works_in(B, D) & (A != B)
teammate(A, B) <= on_project(A, P) & on_project(B, P) & (A != B)

can_ask(A, B) <= colleague(A, B)
can_ask(A, B) <= teammate(A, B)

print(sorted(colleague('ann', B).data))
print(sorted(teammate('ann', B).data))
print(sorted(can_ask('ann', B).data))
print(sorted(can_ask('eli', B).data))
print(colleague('eli', B))
