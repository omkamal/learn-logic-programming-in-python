from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, works_under')

class Employee(pyDatalog.Mixin):
    def __init__(self, name, manager, salary):
        super().__init__()
        self.name, self.manager, self.salary = name, manager, salary
    def __repr__(self):
        return self.name

ann = Employee('ann', None, 150)
bob = Employee('bob', ann, 100)
cid = Employee('cid', bob, 80)

# a clause defines a new attribute on the class
(Employee.manager_name[X] == N) <= (Employee.manager[X] == Y) & (Employee.name[Y] == N)
print(cid.manager_name)
print(bob.manager_name)

# recursion over object attributes
works_under(X, Y) <= (Employee.manager[X] == Y) & (Y != None)
works_under(X, Y) <= (Employee.manager[X] == Z) & works_under(Z, Y)
print(sorted(str(row[0]) for row in works_under(cid, Y).data))

# query objects by attribute
print(sorted(str(row[0]) for row in (Employee.salary[X] > 90).data))
