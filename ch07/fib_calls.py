# Plain Python, the obvious way: count how often fib() is called.
calls = 0

def fib(n):
    global calls
    calls += 1
    return n if n < 2 else fib(n - 1) + fib(n - 2)

for n in (10, 20, 25):
    calls = 0
    print(f'fib({n}) = {fib(n)} after {calls} calls')

a, b = 0, 1                       # fib(101), by a plain loop
for _ in range(101):
    a, b = b, a + b
print(f'fib(100) would need {2 * a - 1} calls')
