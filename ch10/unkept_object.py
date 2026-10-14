from pyDatalog import pyDatalog


class Employee(pyDatalog.Mixin):
    def __init__(self, name, salary):
        super().__init__()
        self.name = name
        self.salary = salary


pyDatalog.create_terms('X, N')

staff = [Employee('ann', 150)]        # kept in a list
Employee('bob', 100)                  # created, but not kept anywhere
dee = Employee('dee', 95)             # kept in a variable

print(sorted(name for _, name in (Employee.name[X] == N).data))
print(len(staff), 'object in the list, and dee is', dee.name)
