from pyDatalog import pyDatalog

pyDatalog.create_terms('T, U, V, S, P, N, sub, member, salary, below')
pyDatalog.create_terms('in_team, team, headcount, payroll, empty')

# sub(team, bigger team) and member(person, team)
for team_, parent in [('engineering', 'acme'), ('operations', 'acme'),
                      ('platform', 'engineering'),
                      ('mobile', 'engineering'), ('web', 'engineering'),
                      ('research', 'engineering'),
                      ('support', 'operations')]:
    +sub(team_, parent)
for person, team_ in [('ann', 'acme'), ('jon', 'engineering'),
                      ('bob', 'platform'), ('cid', 'platform'),
                      ('dee', 'mobile'), ('eli', 'mobile'),
                      ('fay', 'web'), ('gus', 'support'),
                      ('hal', 'support'), ('ivy', 'support')]:
    +member(person, team_)
for person, pay in [('ann', 200), ('jon', 110), ('bob', 120),
                    ('cid', 100), ('dee', 100), ('eli', 90),
                    ('fay', 90), ('gus', 70), ('hal', 70), ('ivy', 60)]:
    +salary(person, pay)

# T is below U: a sub-team, or a sub-team of a sub-team (recursive first)
below(T, U) <= sub(T, U)
below(T, U) <= below(T, V) & sub(V, U)

# a person is in team T directly, or in any team below T
in_team(P, T) <= member(P, T)
in_team(P, T) <= below(S, T) & member(P, S)

# every team that is named anywhere
team(T) <= sub(T, U)
team(U) <= sub(T, U)

# the roll-ups: one number per team, counting each PERSON once
(headcount[T] == len_(P)) <= in_team(P, T)
(payroll[T] == sum_(S, for_each=P)) <= in_team(P, T) & salary(P, S)

# teams nobody is in, however deep
empty(T) <= team(T) & ~in_team(P, T)

for name, n in sorted((headcount[T] == N).data):
    print(f'{name:12} {n:2} people')
print('payroll of engineering:', (payroll['engineering'] == N).data)
print('headcount of research: ', (headcount['research'] == N).data)
print('teams with nobody:     ', sorted(empty(T).data))
