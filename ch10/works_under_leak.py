from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, works_under, leaky')


class Employee(pyDatalog.Mixin):
    def __init__(self, name, manager, salary):
        super().__init__()
        self.name, self.manager, self.salary = name, manager, salary

    def __repr__(self):
        return self.name


ann = Employee('ann', None, 150)
bob = Employee('bob', ann, 100)
cid = Employee('cid', bob, 80)

# slip 1: no filter at all
leaky(X, Y) <= (Employee.manager[X] == Y)
# slip 2: the filter is in the first clause only
works_under(X, Y) <= (Employee.manager[X] == Y) & (Y != None)
works_under(X, Y) <= works_under(X, Z) & (Employee.manager[Z] == Y)


def rows(query):
    return sorted((tuple(None if v is None else str(v) for v in row)
                   for row in query.data), key=str)


print(rows(leaky(X, Y)))
print(rows(works_under(cid, Y)))
