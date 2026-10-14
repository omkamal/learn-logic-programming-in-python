from pyDatalog import pyDatalog

pyDatalog.create_terms('B, M, N, lent_to')


class Member(pyDatalog.Mixin):
    def __init__(self, name):
        super().__init__()
        self.name = name


class Book(pyDatalog.Mixin):
    def __init__(self, title, borrower=None):
        super().__init__()
        self.title, self.borrower = title, borrower


mia = Member('mia')
dune = Book('dune', mia)

# one clause that names two classes and defines a Book attribute
(Book.borrower_name[B] == N) <= (
    (Book.borrower[B] == M) & (Member.name[M] == N))
print(Book.borrower_name[B] == N)
print(dune.borrower_name)

# the cure: an ordinary predicate does the join
lent_to(B, N) <= (Book.borrower[B] == M) & (Member.name[M] == N)
(Book.holder[B] == N) <= lent_to(B, N)
print(dune.holder)
