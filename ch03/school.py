from pyDatalog import pyDatalog

pyDatalog.create_terms('S, S2, C, T, enrolled, teaches, classmate, '
                       'taught_by')

+enrolled('Hana', 'algebra')
+enrolled('Hana', 'biology')
+enrolled('Yusuf', 'algebra')
+enrolled('Mei', 'biology')
+enrolled('Mei', 'chemistry')
+enrolled('Jon', 'chemistry')
+enrolled('Zara', 'biology')

+teaches('Okafor', 'algebra')
+teaches('Okafor', 'chemistry')
+teaches('Silva', 'biology')

classmate(S, S2) <= enrolled(S, C) & enrolled(S2, C) & (S != S2)
taught_by(S, T) <= enrolled(S, C) & teaches(T, C)

print(sorted(classmate('Hana', S2).data))
print(sorted(taught_by('Mei', T).data))
print(sorted(taught_by(S, 'Silva').data))
print(bool(classmate('Jon', 'Yusuf')))
