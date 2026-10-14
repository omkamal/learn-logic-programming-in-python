from pyDatalog import pyDatalog

def slug(title):
    """Lower case, no stray spaces, hyphens between the words."""
    return '-'.join(title.strip().lower().split())

pyDatalog.create_terms('T, U, post, url, slug')

+post('  Hello Logic World ')
+post('Python Inside Rules')

url(T, U) <= post(T) & (U == slug(T))
for row in sorted(url(T, U).data):
    print(row)
