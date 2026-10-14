from pyDatalog import pyDatalog

# clauses inside an ordinary function: the names do not exist there
def setup():
    +road('depot', 'cafe')

try:
    setup()
except NameError as e:
    print('NameError:', e)

# the same idea under the program decorator
@pyDatalog.program()
def _():
    +road('depot', 'cafe')
    +road('cafe', 'school')
    +road('school', 'harbor')
    reach(X, Y) <= road(X, Y)
    reach(X, Y) <= reach(X, Z) & road(Z, Y)

print(sorted(pyDatalog.ask("reach('depot', Y)").answers))

try:
    _()
except TypeError as e:
    print('TypeError:', e)
