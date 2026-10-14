tape = [('ola', 1, 200), ('ola', 2, -150), ('ola', 3, -120),
        ('ola', 5, 300), ('ola', 7, -90), ('ola', 9, -200),
        ('max', 1, 100), ('max', 2, 100), ('max', 4, -50)]

balance = {}
lines = []
for acct, day, amount in sorted(tape):
    balance[acct] = balance.get(acct, 0) + amount
    lines.append((acct, day, amount, balance[acct]))

for line in lines:
    print(line)
