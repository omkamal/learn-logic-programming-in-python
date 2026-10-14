# timeout: 10
from pyDatalog import pyDatalog

pyDatalog.create_terms('N, F, factorial')

factorial[N] = N * factorial[N - 1]     # no ground floor

print('asking for factorial[5] ...')
print(factorial[5] == F)
