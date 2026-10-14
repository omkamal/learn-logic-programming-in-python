import textwrap
from pyDatalog import pyDatalog

pyDatalog.create_terms('P, Q, D, needs, requires')

# needs(package, what it needs directly)
for package, wanted in [
        ('shop', 'web'), ('shop', 'db'),
        ('web', 'http'), ('web', 'templates'),
        ('db', 'driver'), ('db', 'pool'),
        ('http', 'sockets'), ('http', 'tls'),
        ('templates', 'strings'), ('tls', 'crypto'),
        ('pool', 'threads'),
        ('report', 'db'), ('report', 'strings')]:
    +needs(package, wanted)

# P requires D: D is needed directly, or needed by something P requires
requires(P, D) <= needs(P, D)
requires(P, D) <= requires(P, Q) & needs(Q, D)

def names(query):
    return sorted(row[0] for row in query.data)

def show(label, query):
    print(textwrap.fill(' '.join(names(query)), 74,
                        initial_indent=label + ' ',
                        subsequent_indent='    '))

show('to install shop:', requires('shop', D))
show('to install report:', requires('report', D))
show('if tls is removed, these break:', requires(P, 'tls'))
show('if strings is removed:', requires(P, 'strings'))
show('if db is removed:', requires(P, 'db'))
