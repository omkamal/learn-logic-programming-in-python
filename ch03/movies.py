from pyDatalog import pyDatalog

pyDatalog.create_terms('A, B, C, F, acted_in, costar, costar2')

# acted_in(actor, film): invented names and films
+acted_in('Lena Ward', 'Harbor Lights')
+acted_in('Ravi Shah', 'Harbor Lights')
+acted_in('Tomas Pike', 'Harbor Lights')
+acted_in('Lena Ward', 'Winter Orchard')
+acted_in('Nadia Cole', 'Winter Orchard')
+acted_in('Nadia Cole', 'The Long Echo')
+acted_in('Ines Moreau', 'The Long Echo')
+acted_in('Ines Moreau', 'Paper Kites')
+acted_in('Kofi Mensah', 'Paper Kites')

costar(A, B) <= acted_in(A, F) & acted_in(B, F) & (A != B)
costar2(A, C) <= costar(A, B) & costar(B, C) & (A != C)

print(sorted(costar('Lena Ward', B).data))
print(sorted(costar2('Lena Ward', C).data))
print(bool(costar('Lena Ward', 'Ines Moreau')))
print(bool(costar2('Lena Ward', 'Ines Moreau')))
print(bool(costar2('Lena Ward', 'Kofi Mensah')))
