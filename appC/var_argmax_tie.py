# timeout: 90
# Three people tie on 120. Which one does max_(X, order_by=N) return?
import subprocess
import sys

child = """
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, N, Z, emp, best')
for name in ['ann', 'bob', 'cid']:
    +emp(name, 'eng', 120)
(best[Y] == max_(X, order_by=%s)) <= emp(X, Y, N)
print((best['eng'] == Z).data[0][0])
"""
for key in ('N', '(N, X)'):
    seen = set()
    for _ in range(30):
        out = subprocess.run([sys.executable, '-c', child % key],
                             capture_output=True, text=True).stdout
        seen.add(out.strip())
    print('order_by=' + key.ljust(7), 'more than one winner:',
          len(seen) > 1)
    if len(seen) == 1:
        print('    always', seen.pop())
