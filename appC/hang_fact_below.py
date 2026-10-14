# timeout: 8
from pyDatalog import pyDatalog

pyDatalog.create_terms('N, F, factorial')

+(factorial[0] == 1)
factorial[N] = N * factorial[N - 1]
print((factorial[3] == F).data)
print('asking for -1')
print((factorial[-1] == F).data)   # the descent never meets the base
