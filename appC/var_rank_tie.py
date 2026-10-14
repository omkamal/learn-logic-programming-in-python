# timeout: 60
# Two players tie on 880. Who gets rank 0? Ask 16 fresh processes.
import subprocess
import sys

child = """
from pyDatalog import pyDatalog
pyDatalog.create_terms('P, L, S, R, best, rnk')
for p, s in [('leo', 880), ('kai', 880), ('zoe', 700)]:
    +best(p, 'forest', s)
(rnk[P, L] == rank_(group_by=L, order_by=-S)) <= best(P, L, S)
print([p for p, r in sorted((rnk[P, 'forest'] == R).data,
                            key=lambda row: row[1])])
"""
child2 = child.replace('order_by=-S', 'order_by=(-S, P)')
for label, code in (('order_by=-S      ', child),
                    ('order_by=(-S, P) ', child2)):
    seen = set()
    for _ in range(16):
        out = subprocess.run([sys.executable, '-c', code],
                             capture_output=True, text=True).stdout
        seen.add(out.strip())
    print(label, len(seen), 'different order(s)')
