from pyDatalog import pyDatalog

# facts and rules as one block of text (it could be read from a file)
pyDatalog.load("""
+ road('depot', 'cafe')
+ road('cafe', 'school')
reach(X, Y) <= road(X, Y)
reach(X, Y) <= reach(X, Z) & road(Z, Y)
""")
print(sorted(pyDatalog.ask("reach('depot', Y)").answers))
print(pyDatalog.ask("reach('school', Y)"))     # nobody to reach: None

# clear() forgets every fact and clause
pyDatalog.clear()
try:
    pyDatalog.ask("reach('depot', Y)")
except AttributeError as e:
    print('AttributeError:', e)

# load() runs its text as Python code, after a little rewriting
pyDatalog.load("print('this line ran as Python')")
