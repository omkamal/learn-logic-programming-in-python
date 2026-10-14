from pyDatalog import pyDatalog

pyDatalog.create_terms('X, N, pay')


class Employee:
    def __init__(self, name, manager, salary):
        self.name, self.manager, self.salary = name, manager, salary


ann = Employee('ann', None, 150)
bob = Employee('bob', ann, 100)
cid = Employee('cid', bob, 80)

for e in (ann, bob, cid):
    +pay(e.name, e.salary)       # a copy of each object, as a fact

bob.salary = 120                 # the object changes ...
print(bob.salary)
print(sorted(pay('bob', N).data))  # ... but the copy does not
