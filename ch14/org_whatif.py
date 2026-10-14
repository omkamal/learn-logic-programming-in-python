from pyDatalog import pyDatalog

pyDatalog.create_terms('T, U, V, S, P, N, sub, member, salary, below')
pyDatalog.create_terms('in_team, headcount, payroll')

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

(headcount[T] == len_(P)) <= in_team(P, T)
(payroll[T] == sum_(S, for_each=P)) <= in_team(P, T) & salary(P, S)

def counts():
    return dict((headcount[T] == N).data)

print('before:', counts()['engineering'], 'people in engineering')

# dee now also works for the web team
+member('dee', 'web')
now = counts()
print('after: ', now['engineering'], 'people in engineering')
print('mobile', now['mobile'], 'web', now['web'],
      'platform', now['platform'])
print('payroll of engineering:', (payroll['engineering'] == N).data)

# the tempting shortcut: add up the headcounts of the sub-teams
kids = [name for name, in sub(T, 'engineering').data]
direct = len(member(P, 'engineering').data)
print('added up by hand:', direct + sum(now.get(k, 0) for k in kids))
