from pyDatalog import pyDatalog

pyDatalog.create_terms('catalog')
for t in ['emma', 'hamlet', 'ulysses']:
    +catalog(t)

print(bool(catalog('hamlet')))      # there is a card for it
print(bool(catalog('dune')))        # there is no card for it
+catalog('dune')                    # the librarian adds a card
print(bool(catalog('dune')))
