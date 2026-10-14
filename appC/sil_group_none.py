from pyDatalog import pyDatalog

pyDatalog.create_terms('P, A, N, count_all, count_real')


class Pet(pyDatalog.Mixin):
    def __init__(self, name, adopter=None):
        super().__init__()
        self.name, self.adopter = name, adopter


pets = [Pet('bo'), Pet('mia'), Pet('kit', 'hana'), Pet('zig')]

(count_all[A] == len_(P)) <= (Pet.adopter[P] == A)
(count_real[A] == len_(P)) <= (Pet.adopter[P] == A) & (A != None)
print(sorted((count_all[A] == N).data, key=str))
print(sorted((count_real[A] == N).data, key=str))
