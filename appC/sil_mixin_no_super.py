from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N')


class NoSuper(pyDatalog.Mixin):
    def __init__(self, name, salary):
        # super().__init__() is missing here
        self.name, self.salary = name, salary


class Good(pyDatalog.Mixin):
    def __init__(self, name, salary):
        super().__init__()
        self.name, self.salary = name, salary

    def __repr__(self):
        return self.name


NoSuper('ann', 150)
good_ann = Good('ann', 150)

print(NoSuper.salary[X] == N)
print(Good.salary[X] == N)
