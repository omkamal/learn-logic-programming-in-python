from pyDatalog import pyDatalog

pyDatalog.create_terms('S, P, Q, told, spreads')

for a, b in [('mia', 'noor'), ('mia', 'omar'), ('noor', 'pat'),
             ('omar', 'quinn'), ('pat', 'ravi'), ('quinn', 'sam'),
             ('tess', 'pat')]:
    +told(a, b)

spreads(S, P) <= told(S, P)
spreads(S, P) <= spreads(S, Q) & told(Q, P)

def names(query):
    return sorted(row[0] for row in query.data)

print(*names(spreads('mia', P)))
print(*names(spreads('tess', P)))
print(*names(spreads(S, 'ravi')))
