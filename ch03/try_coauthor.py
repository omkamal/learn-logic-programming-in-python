from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, K, wrote, coauthor')

+wrote('Iris', 'Tides')
+wrote('Iris', 'Lanterns')
+wrote('Jon', 'Lanterns')
+wrote('Kai', 'Orchards')
+wrote('Lia', 'Orchards')
+wrote('Lia', 'Tides')

coauthor(A, B) <= wrote(A, K) & wrote(B, K) & (A != B)

print(sorted(coauthor('Iris', B).data))
print(sorted(coauthor('Lia', B).data))
