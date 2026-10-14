from pyDatalog import pyDatalog

pyDatalog.create_terms('E, B, M, reports_to, boss_of')

for e, b in [('ben', 'ana'), ('cleo', 'ana'), ('dev', 'ben'),
             ('eli', 'ben'), ('fay', 'cleo'), ('gus', 'fay')]:
    +reports_to(e, b)

# boss_of(E, B): B is somewhere above E in the chain of command
boss_of(E, B) <= reports_to(E, B)
boss_of(E, B) <= boss_of(E, M) & reports_to(M, B)

print(sorted(boss_of('gus', B).data))
print(sorted(boss_of(E, 'cleo').data))
