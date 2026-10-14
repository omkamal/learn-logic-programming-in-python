from pyDatalog import pyDatalog

pyDatalog.create_terms('B, M, K, count_all, count_members')


class Member(pyDatalog.Mixin):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name


class Book(pyDatalog.Mixin):
    def __init__(self, title, borrower=None):
        super().__init__()
        self.title, self.borrower = title, borrower


mia, leo = Member('mia'), Member('leo')
dune, emma, kim = Book('dune', mia), Book('emma', leo), Book('kim')
hamlet = Book('hamlet', mia)

(count_all[M] == len_(B)) <= (Book.borrower[B] == M)
(count_members[M] == len_(B)) <= (Book.borrower[B] == M) & (M != None)


def rows(query):
    return sorted(((None if m is None else str(m), k)
                   for m, k in query.data), key=str)


print(rows(count_all[M] == K))
print(rows(count_members[M] == K))
