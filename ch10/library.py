from pyDatalog import pyDatalog

pyDatalog.create_terms('B, M, N, K, on_shelf, lent_to, long_loan, loans')


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

on_shelf(B) <= (Book.borrower[B] == None)
lent_to(B, N) <= (Book.borrower[B] == M) & (Member.name[M] == N)
long_loan(M) <= (
    (Book.pages[B] > 300) & (Book.borrower[B] == M) & (M != None))
(loans[M] == len_(B)) <= (Book.borrower[B] == M) & (M != None)


def rows(query):
    return sorted((tuple(v if isinstance(v, int) else str(v) for v in row)
                   for row in query.data), key=str)


print(rows(on_shelf(B)))
print(rows(lent_to(B, N)))
print(rows(long_loan(M)))
print(rows(loans[M] == K))
print(rows(Book.pages[B] > 450))
