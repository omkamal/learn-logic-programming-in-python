# timeout: 10
import textwrap
from pyDatalog import pyDatalog

pyDatalog.create_terms('P, Q, D, needs, requires, cyclic')

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

requires(P, D) <= needs(P, D)
requires(P, D) <= needs(P, Q) & requires(Q, D)    # recursion LAST

def names(query):
    return sorted(row[0] for row in query.data)

def show(label, query):
    print(textwrap.fill(' '.join(names(query)), 74,
                        initial_indent=label + ' ',
                        subsequent_indent='    '))

show('to install shop:', requires('shop', D))
show('if tls is removed:', requires(P, 'tls'))

# three slips by three different teams
for package, wanted in [('shop', 'auth'), ('auth', 'sessions'),
                        ('sessions', 'store'), ('store', 'auth'),
                        ('config', 'logging'), ('logging', 'config')]:
    +needs(package, wanted)

cyclic(P) <= requires(P, P)
print('asking for cycles...')
show('in a cycle:', cyclic(P))
