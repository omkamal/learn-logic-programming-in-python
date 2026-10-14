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

print(len(holds('projects', C).data), 'items under projects')
+contains('img', 'icons')                    # a new subfolder...
+contains('icons', 'home.svg')               # ...with a file inside
print(len(holds('projects', C).data), 'items under projects')
print(bool(holds('web', 'home.svg')))
