from pyDatalog import pyDatalog

pyDatalog.create_terms('P, Q, D, N, needs, requires, dependents')

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

# how many packages are affected if D is removed? (one count per D)
(dependents[D] == len_(P)) <= requires(P, D)

for name, n in sorted((dependents[D] == N).data, key=lambda row: -row[1]):
    print(f'{name:10} {n}')
