from pyDatalog import pyDatalog, pyEngine

pyDatalog.create_terms('X, F, price')

for setting in (8, None, 'Fraction'):
    pyEngine.Float_Precision = setting      # 8 is the default
    pyDatalog.clear()
    +price('a', 0.1)
    +price('b', 12 * 0.14)
    print('Float_Precision =', repr(setting))
    for row in sorted(price(X, F).data):
        print('   ', row)
