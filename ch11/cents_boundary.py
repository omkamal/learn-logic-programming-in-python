from decimal import Decimal

print(19.99 * 100)                 # the float product is a hair low
print(int(19.99 * 100))            # int() cuts the hair off: wrong
print(round(19.99 * 100))          # round() lands on the nearest cent
print(int(Decimal('19.99') * 100)) # text to Decimal to cents: exact
