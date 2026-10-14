from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, N')


class Employee(pyDatalog.Mixin):
    def __init__(self, name, manager, salary):
        super().__init__()
        self.name, self.manager, self.salary = name, manager, salary

    def __repr__(self):
        return self.name


ann = Employee('ann', None, 150)
bob = Employee('bob', ann, 100)
cid = Employee('cid', bob, 80)

(Employee.manager_name[X] == N) <= (
    (Employee.manager[X] == Y) & (Employee.name[Y] == N))

print(cid.manager_name)
print(bob.manager_name)
print(ann.manager_name)
