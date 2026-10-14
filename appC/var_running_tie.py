# timeout: 60
# Two payments fall on the same day; the order of the facts is swapped.
import subprocess
import sys

child = """
from pyDatalog import pyDatalog
pyDatalog.create_terms('T, A, D, N, S, tx, bal')
+tx('t1', 'ola', 1, 200)
for t, d, n in %s:
    +tx(t, 'ola', d, n)
(bal[T] == running_sum_(N, group_by=A, order_by=%s)) <= tx(T, A, D, N)
print(sorted((bal[T] == S).data))
"""
rent, coffee = ('t3', 3, -120), ('t4', 3, -20)
for facts in ([rent, coffee], [coffee, rent]):
    for key in ('D', '(D, T)'):
        seen = set()
        for _ in range(6):
            run = subprocess.run([sys.executable, '-c',
                                  child % (facts, key)],
                                 capture_output=True, text=True)
            seen.add(run.stdout.strip() or run.stderr.strip()[-60:])
        print([f[0] for f in facts], 'order_by=' + key)
        for line in sorted(seen):
            print('    ', line)
