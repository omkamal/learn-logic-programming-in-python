from pyDatalog import pyDatalog

pyDatalog.create_terms('S, S2, C, T, enrolled, teaches, classmate, '
                       'taught_by')

+enrolled('Hana', 'algebra')
+enrolled('Hana', 'biology')
+enrolled('Mei', 'biology')
+enrolled('Mei', 'chemistry')
+enrolled('Zara', 'biology')
+teaches('Okafor', 'chemistry')
+teaches('Silva', 'biology')

classmate(S, S2) <= enrolled(S, C) & enrolled(S2, C) & (S != S2)
taught_by(S, T) <= enrolled(S, C) & teaches(T, C)

print(sorted(classmate('Hana', S2).data), sorted(taught_by('Zara', T).data))
pyDatalog.retract_fact('enrolled', 'Zara', 'biology')
pyDatalog.assert_fact('enrolled', 'Zara', 'chemistry')
print(sorted(classmate('Hana', S2).data), sorted(taught_by('Zara', T).data))
