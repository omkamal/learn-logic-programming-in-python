from pyDatalog import pyDatalog

pyDatalog.create_terms('B, M, N, Y, lent_to, veteran_loan')


class Member(pyDatalog.Mixin):
    def __init__(self, name, joined):
        super().__init__()
        self.name, self.joined = name, joined

    def __repr__(self):
        return self.name


class Book(pyDatalog.Mixin):
    def __init__(self, title, borrower=None):
        super().__init__()
        self.title, self.borrower = title, borrower

    def __repr__(self):
        return self.title


mia, leo = Member('mia', 2018), Member('leo', 2022)
dune, emma = Book('dune', mia), Book('emma', leo)
kim = Book('kim')

veteran_loan(M) <= (Member.joined[M] < 2020) & (Book.borrower[B] == M)
print(sorted(str(row[0]) for row in veteran_loan(M).data))
