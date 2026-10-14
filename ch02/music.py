from pyDatalog import pyDatalog

pyDatalog.create_terms('Title, Artist, Genre, album')

# album(title, artist, genre): one card per album, three slots
+album('Blue Harbor', 'Mira Lane', 'jazz')
+album('Night Trains', 'Mira Lane', 'jazz')
+album('Slow Hours', 'Tomas Reyes', 'jazz')
+album('Paper Moons', 'The Lanterns', 'folk')
+album('Salt and Thread', 'The Lanterns', 'folk')
+album('Static Garden', 'Orbit Seven', 'electronic')
+album('Glass Rivers', 'Orbit Seven', 'electronic')

print(album(Title, 'Mira Lane', Genre))
print(album('Static Garden', Artist, Genre))
for row in sorted(album(Title, Artist, 'jazz').data):
    print(row)
print(bool(album('Paper Moons', Artist, Genre)))
print(bool(album('Paper Moons', 'Orbit Seven', Genre)))
