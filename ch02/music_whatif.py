from pyDatalog import pyDatalog

pyDatalog.create_terms('Title, Artist, Genre, album')

+album('Blue Harbor', 'Mira Lane', 'jazz')
+album('Night Trains', 'Mira Lane', 'jazz')
+album('Slow Hours', 'Tomas Reyes', 'jazz')
+album('Paper Moons', 'The Lanterns', 'folk')

print(len(album(Title, Artist, 'jazz').data), 'jazz albums')
+album('Midnight Brass', 'Tomas Reyes', 'jazz')     # one new card
print(len(album(Title, Artist, 'jazz').data), 'jazz albums')
print(sorted(album(Title, 'Tomas Reyes', Genre).data))
