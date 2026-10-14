import textwrap
from pyDatalog import pyDatalog

pyDatalog.create_terms('M, B, T')


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

# a Member attribute built from Book literals only
(Member.book_title[M] == T) <= (
    (Book.borrower[B] == M) & (Book.title[B] == T))
try:
    print(Member.book_title[M] == T)
except Exception as err:
    print(textwrap.fill(type(err).__name__ + ': ' + str(err), 74,
                        subsequent_indent='    '))
