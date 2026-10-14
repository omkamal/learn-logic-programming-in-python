from pyDatalog import pyDatalog

text = "+shop('Mia's Corner')"     # an apostrophe inside the text
try:
    pyDatalog.load(text)
except Exception as err:
    print(type(err).__name__ + ':', err)
