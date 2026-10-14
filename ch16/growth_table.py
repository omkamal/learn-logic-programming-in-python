# timeout: 150
import subprocess
import sys

cases = [('chain', 25), ('chain', 50), ('chain', 100), ('chain', 200),
         ('chain', 400), ('chain', 800), ('chain', 1600),
         ('ring', 400), ('tree', 1023), ('tree', 8191)]

print('shape   links    pairs  seconds  peak MB  microseconds per pair')
for shape, n in cases:
    command = [sys.executable, '_growth_child.py', shape, str(n)]
    run = subprocess.run(command, capture_output=True, text=True)
    name, links, pairs, seconds, peak = run.stdout.split()
    per_pair = 1e6 * float(seconds) / int(pairs)
    print('%-5s %7s %8s %8.2f %8s %12.1f' % (
        name, links, pairs, float(seconds), peak, per_pair))
