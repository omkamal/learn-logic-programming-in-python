from pyDatalog import pyDatalog

try:
    pyDatalog.load("+ shop('Mira's corner')")   # apostrophe inside the text
except SyntaxError as e:
    print('SyntaxError:', e)

pyDatalog.assert_fact('shop', "Mira's corner")    # as a value: no problem
pyDatalog.create_terms('X, shop')
print(shop(X).data)
