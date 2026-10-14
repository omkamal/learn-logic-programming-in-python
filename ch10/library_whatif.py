from pyDatalog import pyDatalog

pyDatalog.create_terms('B, M, N, K, on_shelf, loans')


class Member(pyDatalog.Mixin):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name


class Book(pyDatalog.Mixin):
    def __init__(self, title, pages, borrower=None):
        super().__init__()
        self.title, self.pages, self.borrower = title, pages, borrower

    def __repr__(self):
        return self.title


mia, leo = Member('mia'), Member('leo')
dune = Book('dune', 612, mia)
emma = Book('emma', 474, leo)
hamlet = Book('hamlet', 160, mia)
walden = Book('walden', 352)

on_shelf(B) <= (Book.borrower[B] == None)
(loans[M] == len_(B)) <= (Book.borrower[B] == M) & (M != None)


def rows(query):
    return sorted((tuple(v if isinstance(v, int) else str(v) for v in row)
                   for row in query.data), key=str)


print(rows(on_shelf(B)), rows(loans[M] == K))
emma.borrower = None                       # leo brings emma back
print(rows(on_shelf(B)), rows(loans[M] == K))
