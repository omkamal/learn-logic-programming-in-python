from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, works_under')


class Employee(pyDatalog.Mixin):
    def __init__(self, name, manager=None):
        super().__init__()
        self.name, self.manager = name, manager

    def __repr__(self):
        return self.name


ann = Employee('ann')
bob = Employee('bob', ann)
cid = Employee('cid', bob)

# the filter is in the base clause only
works_under(X, Y) <= (Employee.manager[X] == Y) & (Y != None)
works_under(X, Y) <= works_under(X, Z) & (Employee.manager[Z] == Y)
print(sorted(works_under(cid, Y).data, key=str))
