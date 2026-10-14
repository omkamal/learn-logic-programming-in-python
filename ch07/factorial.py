from pyDatalog import pyDatalog

pyDatalog.create_terms('N, F, factorial')

+(factorial[0] == 1)                  # the ground floor
factorial[N] = N * factorial[N - 1]   # one step up

print(factorial[5] == F)
print(factorial[10] == F)
