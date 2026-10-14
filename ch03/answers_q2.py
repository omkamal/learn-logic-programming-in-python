from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, D, works_in, colleague, colleague2')

+works_in('ann', 'eng')
+works_in('bob', 'eng')

colleague(A, B) <= works_in(A, D) & works_in(B, D)
colleague2(A, B) <= works_in(A, D) & works_in(B, D) & (A != B)

print(sorted(colleague('ann', B).data))
print(sorted(colleague2('ann', B).data))
