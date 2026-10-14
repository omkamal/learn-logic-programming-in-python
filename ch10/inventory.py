from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, W, I, P, inside_of, load, heavy_owner')


class Player(pyDatalog.Mixin):
    def __init__(self, name, level):
        super().__init__()
        self.name, self.level = name, level

    def __repr__(self):
        return self.name


class Item(pyDatalog.Mixin):
    def __init__(self, name, weight, owner, inside=None):
        super().__init__()
        self.name, self.weight = name, weight
        self.owner, self.inside = owner, inside

    def __repr__(self):
        return self.name


hero, mage = Player('hero', 7), Player('mage', 3)
backpack = Item('backpack', 2, hero)
pouch = Item('pouch', 1, hero, backpack)
potion = Item('potion', 1, hero, pouch)
gem = Item('gem', 1, hero, pouch)
rope = Item('rope', 3, hero, backpack)
sword = Item('sword', 5, hero)
staff = Item('staff', 4, mage)

inside_of(X, Y) <= (Item.inside[X] == Y) & (Y != None)
inside_of(X, Y) <= (
    inside_of(X, Z) & (Item.inside[Z] == Y) & (Y != None))
(load[P] == sum_(W, for_each=I)) <= (
    (Item.owner[I] == P) & (Item.weight[I] == W))
heavy_owner(P) <= (Item.weight[I] > 3) & (Item.owner[I] == P)


def rows(query):
    return sorted((tuple(v if isinstance(v, int) else str(v) for v in row)
                   for row in query.data), key=str)


print(rows(inside_of(X, backpack)))
print(rows(inside_of(potion, Y)))
print(rows(load[P] == W))
print(rows(heavy_owner(P)))
