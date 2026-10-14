import sys
import time
from pyDatalog import pyDatalog, pyEngine

engine = pyEngine.__file__.rsplit('/', 1)[-1]
print('Python', sys.version.split()[0], '| engine file:', engine)

pyDatalog.create_terms('X, Y, Z, link, reach')
for i in range(400):
    +link(i, i + 1)
reach(X, Y) <= link(X, Y)
reach(X, Y) <= reach(X, Z) & link(Z, Y)

start = time.perf_counter()
pairs = len(reach(X, Y).data)
seconds = time.perf_counter() - start
print('chain of 400 links:', pairs, 'pairs in', round(seconds, 2), 's')
