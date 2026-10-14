from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, inside_of')


class Item(pyDatalog.Mixin):
    def __init__(self, name, weight, inside=None):
        super().__init__()
        self.name, self.weight, self.inside = name, weight, inside

    def __repr__(self):
        return self.name


backpack = Item('backpack', 2)
pouch = Item('pouch', 1, backpack)
potion = Item('potion', 1, pouch)
gem = Item('gem', 1, pouch)
rope = Item('rope', 3, backpack)
purse = Item('purse', 1, backpack)

inside_of(X, Y) <= (Item.inside[X] == Y) & (Y != None)
inside_of(X, Y) <= (
    inside_of(X, Z) & (Item.inside[Z] == Y) & (Y != None))


def rows(query):
    return sorted(tuple(str(v) for v in row) for row in query.data)


def show():
    print('pouch', rows(inside_of(X, pouch)),
          'purse', rows(inside_of(X, purse)))
    print('backpack', rows(inside_of(X, backpack)))


show()
potion.inside = purse                     # move the potion to the purse
show()
