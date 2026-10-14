from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, pay')


class Employee(pyDatalog.Mixin):
    def __init__(self, name, salary):
        super().__init__()
        self.name, self.salary = name, salary

    def __repr__(self):
        return self.name


staff = [Employee('ann', 150), Employee('bob', 100)]
for e in staff:
    +pay(e.name, e.salary)         # a copy: a photograph of the objects

staff[1].salary = 120              # a raise, inside the program
print(sorted((pay(X, N)).data))
print(sorted((Employee.salary[X] == N).data, key=str))
