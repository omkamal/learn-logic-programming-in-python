from pyDatalog import pyDatalog


def setup():
    +road('depot', 'cafe')         # road was never created


try:
    setup()
except Exception as err:
    print(type(err).__name__ + ':', err)
