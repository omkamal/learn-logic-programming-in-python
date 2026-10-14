from pyDatalog import pyDatalog

pyDatalog.create_terms('P, N')


class Player(pyDatalog.Mixin):
    def __init__(self, name, level):
        self.name = name
        self.level = level


zoe = Player('zoe', 7)
leo = Player('leo', 3)

print(Player.level[P] == N)
