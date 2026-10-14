class Employee:
    def __init__(self, name, manager, salary):
        self.name, self.manager, self.salary = name, manager, salary


ann = Employee('ann', None, 150)
bob = Employee('bob', ann, 100)
cid = Employee('cid', bob, 80)


def bosses(person):
    found = []
    while person.manager is not None:
        person = person.manager
        found.append(person.name)
    return found


print(bosses(cid))
print([p.name for p in (ann, bob, cid) if p.salary > 90])
