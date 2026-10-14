from pyDatalog import pyDatalog

pyDatalog.create_terms('P, A, K, count_all, count_real')


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

(count_all[A] == len_(P)) <= (Pet.adopter[P] == A)
(count_real[A] == len_(P)) <= (Pet.adopter[P] == A) & (A != None)


def plain(value):
    return value if value is None or isinstance(value, int) else str(value)


def rows(query):
    return sorted((tuple(plain(v) for v in row) for row in query.data),
                  key=str)


print(rows(count_all[A] == K))
print(rows(count_real[A] == K))
