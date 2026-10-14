# timeout: 10
from pyDatalog import pyDatalog

pyDatalog.create_terms('N, F, factorial')

+(factorial[0] == 1)
factorial[N] = N * factorial[N - 1]

print('asking for factorial[-1] ...')
print(factorial[-1] == F)
