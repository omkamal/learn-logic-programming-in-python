from pyDatalog import pyDatalog

pyDatalog.create_terms('T, U, S, P, X, Y, Z, N, under, in_org, headcount')

class Team(pyDatalog.Mixin):
    def __init__(self, name, parent):
        super().__init__()
        self.name, self.parent = name, parent
    def __repr__(self):
        return self.name

class Person(pyDatalog.Mixin):
    def __init__(self, name, team):
        super().__init__()
        self.name, self.team = name, team
    def __repr__(self):
        return self.name

acme = Team('acme', None)
eng = Team('engineering', acme)
ops = Team('operations', acme)
platform = Team('platform', eng)
support = Team('support', ops)
everyone = [Person('ann', acme), Person('jon', eng),
            Person('bob', platform), Person('cid', platform),
            Person('gus', support)]       # keep a reference to each one!

# T is under U: its parent is U, or its parent is under U (recursive first)
under(X, Y) <= (Team.parent[X] == Y) & (Y != None)
under(X, Y) <= under(X, Z) & (Team.parent[Z] == Y) & (Y != None)

# a person is in a team directly, or in any team under it
in_org(P, T) <= (Person.team[P] == T)
in_org(P, T) <= under(S, T) & (Person.team[P] == S)
(headcount[T] == len_(P)) <= in_org(P, T)

print('engineering holds:', sorted(str(p) for p, in in_org(P, eng).data))
for team, n in sorted((str(t), n) for t, n in (headcount[T] == N).data):
    print(f'{team:12} {n}')
