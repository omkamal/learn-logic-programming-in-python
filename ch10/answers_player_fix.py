from pyDatalog import pyDatalog

pyDatalog.create_terms('P, N')


class Player(pyDatalog.Mixin):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level

    def __repr__(self):
        return self.name


zoe = Player('zoe', 7)
leo = Player('leo', 3)

print(sorted((str(p), n) for p, n in (Player.level[P] == N).data))
