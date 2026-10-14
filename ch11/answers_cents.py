prices = [19.99, 5.05, 0.10]

print(sum(prices))                       # floats, plain Python
cents = [round(p * 100) for p in prices]
print(cents, sum(cents))                 # whole cents
print('%d.%02d' % (sum(cents) // 100, sum(cents) % 100))
