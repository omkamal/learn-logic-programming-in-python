from pyDatalog import pyDatalog

pyDatalog.create_terms('T, U, V, S, P, N, sub, member, below, in_team')
pyDatalog.create_terms('team, headcount, empty')

for team_, parent in [('engineering', 'acme'), ('operations', 'acme'),
                      ('platform', 'engineering'),
                      ('mobile', 'engineering'), ('web', 'engineering'),
                      ('research', 'engineering'),
                      ('support', 'operations'),
                      ('qa', 'engineering')]:      # the new team
    +sub(team_, parent)
for person, team_ in [('ann', 'acme'), ('jon', 'engineering'),
                      ('bob', 'platform'), ('cid', 'platform'),
                      ('dee', 'mobile'), ('eli', 'mobile'),
                      ('fay', 'web'), ('gus', 'support'),
                      ('hal', 'support'), ('ivy', 'support')]:
    +member(person, team_)

below(T, U) <= sub(T, U)
below(T, U) <= below(T, V) & sub(V, U)
in_team(P, T) <= member(P, T)
in_team(P, T) <= below(S, T) & member(P, S)
team(T) <= sub(T, U)
team(U) <= sub(T, U)
(headcount[T] == len_(P)) <= in_team(P, T)
empty(T) <= team(T) & ~in_team(P, T)

print('headcount of qa:', (headcount['qa'] == N).data)
print('teams with nobody:', sorted(empty(T).data))
