from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, works_under')


class Employee(pyDatalog.Mixin):
    def __init__(self, name, manager):
        super().__init__()
        self.name, self.manager = name, manager

    def __repr__(self):
        return self.name


ann = Employee('ann', None)
bob, cid = Employee('bob', ann), Employee('cid', ann)
dee, fay = Employee('dee', bob), Employee('fay', cid)
eli = Employee('eli', dee)

works_under(X, Y) <= (Employee.manager[X] == Y) & (Y != None)
works_under(X, Y) <= (
    works_under(X, Z) & (Employee.manager[Z] == Y) & (Y != None))


def names(query):
    return sorted(str(row[0]) for row in query.data)


print(names(works_under(X, bob)), names(works_under(X, ann)))
print(names(works_under(eli, Y)))
gus = Employee('gus', fay)                 # a new hire: no new rule
print(names(works_under(gus, Y)), names(works_under(X, cid)))
