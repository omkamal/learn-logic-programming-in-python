from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N')


class NoSuper(pyDatalog.Mixin):
    def __init__(self, name, salary):
        # super().__init__() is missing here
        self.name, self.salary = name, salary


class NoMixin:
    def __init__(self, name, salary):
        self.name, self.salary = name, salary


NoSuper('ann', 150)
NoMixin('ann', 150)

print(NoSuper.salary[X] == N)
try:
    print(NoMixin.salary[X] == N)
except Exception as err:
    print(type(err).__name__ + ':', err)
