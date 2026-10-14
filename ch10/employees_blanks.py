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

print(sorted((Employee.salary[bob] == N).data))
print(sorted((Employee.manager[cid] == Y).data, key=str))
print(bool(Employee.manager[cid] == bob))
print(bool(Employee.manager[cid] == ann))
print(sorted((Employee.salary[X] == 80).data, key=str))
