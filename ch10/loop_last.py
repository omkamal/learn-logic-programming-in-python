# timeout: 10
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, works_under')


class Employee(pyDatalog.Mixin):
    def __init__(self, name, manager, salary):
        super().__init__()
        self.name, self.manager, self.salary = name, manager, salary

    def __repr__(self):
        return self.name


ann = Employee('ann', None, 150)
bob = Employee('bob', ann, 100)
cid = Employee('cid', bob, 80)
ann.manager = cid          # a data-entry slip: ann -> cid -> bob -> ann

works_under(X, Y) <= (Employee.manager[X] == Y) & (Y != None)
works_under(X, Y) <= (Employee.manager[X] == Z) & works_under(Z, Y)

print(sorted(str(row[0]) for row in works_under(cid, Y).data))
