from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N')


class Employee(pyDatalog.Mixin):
    def __init__(self, name, salary):
        super().__init__()
        self.name, self.salary = name, salary

    def __repr__(self):
        return self.name


staff = [Employee('ann', 150)]
Employee('bob', 100)               # created, but kept nowhere
dee = Employee('dee', 95)

print(sorted((Employee.salary[X] > 90).data, key=str))
