import textwrap
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, flight, reach')
+flight('CAI', 'DXB')
reach(X, Y) <= flight(X, Y)
print(reach('CAI', Y))

pyDatalog.clear()                  # forget every fact and every rule
try:
    print(reach('CAI', Y))
except Exception as err:
    print(textwrap.fill(type(err).__name__ + ': ' + str(err), 74,
                        subsequent_indent='    '))
