from decimal import Decimal

print(0.5 + 0.25)           # halves and quarters are exact in binary
print(0.1 + 0.2)            # tenths are not

total = 0.0
for _ in range(10):         # ten dimes
    total += 0.1
print(total)                # not exactly one dollar

print(Decimal(0.1))         # what Python really stores for 0.1
