import textwrap
from pyDatalog import pyDatalog

pyDatalog.create_terms('P, Q, D, needs, requires, cyclic, stuck')

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
requires(P, D) <= requires(P, Q) & needs(Q, D)

# P is in a cycle when it ends up requiring itself
cyclic(P) <= requires(P, P)
# stuck: in a cycle, or needs something that is in one
stuck(P) <= cyclic(P)
stuck(P) <= requires(P, Q) & cyclic(Q)

def names(query):
    return sorted(row[0] for row in query.data)

def show(label, query):
    print(textwrap.fill(' '.join(names(query)), 74,
                        initial_indent=label + ' ',
                        subsequent_indent='    '))

print('cycles before the slips:', names(cyclic(P)))

# three slips by three different teams
for package, wanted in [('shop', 'auth'), ('auth', 'sessions'),
                        ('sessions', 'store'), ('store', 'auth'),
                        ('config', 'logging'), ('logging', 'config')]:
    +needs(package, wanted)

show('in a cycle:', cyclic(P))
show('stuck:     ', stuck(P))
show('shop needs:', requires('shop', D))
print('report is stuck?', bool(stuck('report')))
show('auth needs:', requires('auth', D))
