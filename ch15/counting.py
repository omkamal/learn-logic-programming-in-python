from math import comb, factorial

print('any 8 of the 64 squares:    ', comb(64, 8))
print('one queen in every row:     ', 8 ** 8)
print('... and no shared column:   ', factorial(8))
