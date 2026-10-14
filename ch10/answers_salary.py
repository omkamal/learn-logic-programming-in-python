from pyDatalog import pyDatalog

pyDatalog.create_terms('X')


class Employee(pyDatalog.Mixin):
    def __init__(self, name, manager, salary):
        super().__init__()
        self.name, self.manager, self.salary = name, manager, salary

    def __repr__(self):
        return self.name


ann = Employee('ann', None, 150)
bob = Employee('bob', ann, 100)
cid = Employee('cid', bob, 80)

bob.salary = 95
cid.salary = 120
print(sorted(str(row[0]) for row in (Employee.salary[X] > 90).data))
