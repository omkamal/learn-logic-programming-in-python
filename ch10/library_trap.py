import textwrap

from pyDatalog import pyDatalog

pyDatalog.create_terms('B, M, N, T, lent_to')


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
walden = Book('walden')

# slip: one clause that names two classes and defines a Book attribute
(Book.borrower_name[B] == N) <= (
    (Book.borrower[B] == M) & (Member.name[M] == N))
print(Book.borrower_name[B] == N)
print(dune.borrower_name)

# the same slip turned around: a Member attribute built from Book literals
(Member.book_title[M] == T) <= (
    (Book.borrower[B] == M) & (Book.title[B] == T))
try:
    print(Member.book_title[M] == T)
except Exception as err:
    print(textwrap.fill(type(err).__name__ + ': ' + str(err), 74))

# fix: let an ordinary predicate do the join across classes
lent_to(B, N) <= (Book.borrower[B] == M) & (Member.name[M] == N)
(Book.holder[B] == N) <= lent_to(B, N)
print(dune.holder)
