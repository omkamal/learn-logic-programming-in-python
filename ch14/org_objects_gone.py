from pyDatalog import pyDatalog

pyDatalog.create_terms('P, T, in_org')

class Team(pyDatalog.Mixin):
    def __init__(self, name):
        super().__init__()
        self.name = name

class Person(pyDatalog.Mixin):
    def __init__(self, name, team):
        super().__init__()
        self.name, self.team = name, team
    def __repr__(self):
        return self.name

platform = Team('platform')
bob = Person('bob', platform)          # kept in a variable
Person('cid', platform)                # created, but never kept

in_org(P, T) <= (Person.team[P] == T)
print(sorted(str(p) for p, in in_org(P, platform).data))
