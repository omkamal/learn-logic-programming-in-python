from pyDatalog import pyDatalog

pyDatalog.create_terms('P, Q, D, needs, requires')

for package, wanted in [
        ('shop', 'web'), ('shop', 'db'),
        ('web', 'http'), ('web', 'templates'),
        ('db', 'driver'), ('db', 'pool'),
        ('http', 'sockets'), ('http', 'tls'),
        ('templates', 'strings'), ('tls', 'crypto'),
        ('pool', 'threads'),
        ('report', 'db'), ('report', 'strings')]:
    +needs(package, wanted)

requires(P, D) <= needs(P, D)
requires(P, D) <= requires(P, Q) & needs(Q, D)

print('crypto removed, these break:',
      sorted(row[0] for row in requires(P, 'crypto').data))
print('shop needs crypto?', bool(requires('shop', 'crypto')))
print('report needs crypto?', bool(requires('report', 'crypto')))
