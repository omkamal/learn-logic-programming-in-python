contains = [('projects', 'web'), ('projects', 'data'),
            ('projects', 'notes.txt'), ('web', 'css'),
            ('web', 'img'), ('web', 'index.html'),
            ('css', 'main.css'), ('img', 'logo.png'),
            ('data', 'raw'), ('data', 'report.pdf'),
            ('raw', 'sales.csv')]

notebook = set(contains)
print('round 1:', len(notebook), 'new')
n = 1
while True:
    n += 1
    new = {(x, y) for (x, z) in notebook
                  for (z2, y) in contains if z == z2} - notebook
    print(f'round {n}:', len(new), 'new')
    if ('projects', 'sales.csv') in new:
        print('  projects-sales.csv is written in round', n)
    if not new:
        break
    notebook |= new
