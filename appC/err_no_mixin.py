from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N')


class NoMixin:                     # forgot to inherit from pyDatalog.Mixin
    def __init__(self, name, salary):
        self.name, self.salary = name, salary


NoMixin('ann', 150)
try:
    print(NoMixin.salary[X] == N)
except Exception as err:
    print(type(err).__name__ + ':', err)
