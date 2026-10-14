from pyDatalog import pyDatalog

pyDatalog.create_terms('P, A, C, N, M, K, waiting, young, per_city')


class Adopter(pyDatalog.Mixin):
    def __init__(self, name, city):
        super().__init__()
        self.name, self.city = name, city

    def __repr__(self):
        return self.name


class Pet(pyDatalog.Mixin):
    def __init__(self, name, species, age, adopter=None):
        super().__init__()
        self.name, self.species, self.age = name, species, age
        self.adopter = adopter

    def __repr__(self):
        return self.name


hana, omar = Adopter('hana', 'Leeds'), Adopter('omar', 'York')
rex = Pet('rex', 'dog', 3, hana)
kit = Pet('kit', 'cat', 2, omar)
mia = Pet('mia', 'cat', 1)
bo = Pet('bo', 'dog', 7)
ziggy = Pet('ziggy', 'dog', 1)

waiting(P) <= (Pet.adopter[P] == None)
(Pet.months[P] == M) <= (Pet.age[P] == N) & (M == N * 12)
young(P) <= (Pet.months[P] < 24) & (Pet.adopter[P] == None)
(per_city[C] == len_(P)) <= (Pet.adopter[P] == A) & (Adopter.city[A] == C)


def plain(value):
    return value if value is None or isinstance(value, int) else str(value)


def rows(query):
    return sorted((tuple(plain(v) for v in row) for row in query.data),
                  key=str)


print(rows(waiting(P)))
print(rows(Pet.months[P] == M))
print(rows(young(P)))
print(rows(per_city[C] == K))
