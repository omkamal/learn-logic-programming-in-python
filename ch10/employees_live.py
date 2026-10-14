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


def rows(query):
    return sorted((tuple(None if v is None else str(v) for v in row)
                   for row in query.data), key=str)


print(rows(Employee.salary[X] > 90))
bob.salary = 60                                 # change an attribute
print(rows(Employee.salary[X] > 90))
dee = Employee('dee', ann, 95)                  # create another object
print(rows(Employee.salary[X] > 90))
