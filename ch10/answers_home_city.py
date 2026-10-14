from pyDatalog import pyDatalog

pyDatalog.create_terms('P, A, N, home')


class Adopter(pyDatalog.Mixin):
    def __init__(self, name, city):
        super().__init__()
        self.name, self.city = name, city


class Pet(pyDatalog.Mixin):
    def __init__(self, name, adopter=None):
        super().__init__()
        self.name, self.adopter = name, adopter


hana = Adopter('hana', 'Leeds')
rex = Pet('rex', hana)

(Pet.home_city[P] == N) <= (Pet.adopter[P] == A) & (Adopter.city[A] == N)
print(rex.home_city)

home(P, N) <= (Pet.adopter[P] == A) & (Adopter.city[A] == N)
(Pet.town[P] == N) <= home(P, N)
print(rex.town)
