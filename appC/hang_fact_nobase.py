# timeout: 8
from pyDatalog import pyDatalog

pyDatalog.create_terms('N, F, factorial')

# the ground floor +(factorial[0] == 1) is missing
factorial[N] = N * factorial[N - 1]
print('asking')
print((factorial[5] == F).data)
