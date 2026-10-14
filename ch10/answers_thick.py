from pyDatalog import pyDatalog

pyDatalog.create_terms('B, M, N, K, lent_to, thick')


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
kim = Book('kim', 250)

lent_to(B, N) <= (Book.borrower[B] == M) & (Member.name[M] == N)
thick(B, N) <= (Book.pages[B] > 300) & lent_to(B, N)

print(sorted((str(b), n) for b, n in thick(B, N).data))
