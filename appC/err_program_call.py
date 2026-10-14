from pyDatalog import pyDatalog


@pyDatalog.program()
def _():
    +road('depot', 'cafe')
    reach(X, Y) <= road(X, Y)


print(pyDatalog.ask("reach('depot', Y)").answers)
try:
    _()                            # a datalog program runs once, at load
except Exception as err:
    print(type(err).__name__ + ':', err)
