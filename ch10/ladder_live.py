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

(Employee.manager_name[X] == Y) <= (
    (Employee.manager[X] == Z) & (Employee.name[Z] == Y))
works_under(X, Y) <= (Employee.manager[X] == Y) & (Y != None)
works_under(X, Y) <= (
    works_under(X, Z) & (Employee.manager[Z] == Y) & (Y != None))


def names(query):
    return sorted(str(row[0]) for row in query.data)


print(names(works_under(cid, Y)), cid.manager_name)
cid.manager = ann                               # move cid under ann
print(names(works_under(cid, Y)), cid.manager_name)
