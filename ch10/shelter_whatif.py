from pyDatalog import pyDatalog

pyDatalog.create_terms('P, A, C, K, waiting, per_city')


class Adopter(pyDatalog.Mixin):
    def __init__(self, name, city):
        super().__init__()
        self.name, self.city = name, city

    def __repr__(self):
        return self.name


class Pet(pyDatalog.Mixin):
    def __init__(self, name, adopter=None):
        super().__init__()
        self.name, self.adopter = name, adopter

    def __repr__(self):
        return self.name


hana, omar = Adopter('hana', 'Leeds'), Adopter('omar', 'York')
rex, kit = Pet('rex', hana), Pet('kit', omar)
mia, bo = Pet('mia'), Pet('bo')

waiting(P) <= (Pet.adopter[P] == None)
(per_city[C] == len_(P)) <= (Pet.adopter[P] == A) & (Adopter.city[A] == C)


def rows(query):
    return sorted((tuple(v if isinstance(v, int) else str(v) for v in row)
                   for row in query.data), key=str)


print(rows(waiting(P)), rows(per_city[C] == K))
mia.adopter = hana                         # hana adopts mia
print(rows(waiting(P)), rows(per_city[C] == K))
