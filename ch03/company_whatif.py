from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, D, works_in, colleague')

+works_in('ann', 'eng')
+works_in('bob', 'eng')
+works_in('eli', 'hr')

colleague(A, B) <= works_in(A, D) & works_in(B, D) & (A != B)

print(sorted(colleague('eli', B).data))
pyDatalog.retract_fact('works_in', 'eli', 'hr')
pyDatalog.assert_fact('works_in', 'eli', 'eng')
print(sorted(colleague('eli', B).data))
print(sorted(colleague('ann', B).data))
