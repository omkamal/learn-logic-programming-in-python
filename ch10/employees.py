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


def plain(value):
    return value if value is None or isinstance(value, int) else str(value)


def rows(query):
    return sorted((tuple(plain(v) for v in row) for row in query.data),
                  key=str)


print(rows(Employee.salary[X] > 90))
print(rows(Employee.manager[X] == Y))
print(rows(Employee.manager[X] == ann))
print(rows(Employee.name[X] == 'cid'))
