from pyDatalog import pyDatalog

pyDatalog.create_terms('F, G, C, contains, holds')

for folder, item in [('projects', 'web'), ('projects', 'data'),
                     ('projects', 'notes.txt'), ('web', 'css'),
                     ('web', 'img'), ('web', 'index.html'),
                     ('css', 'main.css'), ('img', 'logo.png'),
                     ('data', 'raw'), ('data', 'report.pdf'),
                     ('raw', 'sales.csv')]:
    +contains(folder, item)

holds(F, C) <= contains(F, C)
holds(F, C) <= holds(F, G) & contains(G, C)

def names(query):
    return sorted(row[0] for row in query.data)

print(*names(holds('web', C)))
print(len(names(holds('projects', C))), 'items under projects')
print(*names(holds(F, 'logo.png')))
