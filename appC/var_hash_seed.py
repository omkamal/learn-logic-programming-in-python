# timeout: 60
# Is the hash seed what decides the order? Fix it, and ask 12 times.
import os
import subprocess
import sys

child = """
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, parent')
+parent('alice', 'bob')
+parent('alice', 'carol')
print(parent('alice', X).data)
"""
for seed in ('0', '1', '2'):
    env = dict(os.environ, PYTHONHASHSEED=seed)
    seen = set()
    for _ in range(12):
        out = subprocess.run([sys.executable, '-c', child], env=env,
                             capture_output=True, text=True).stdout
        seen.add(out.strip())
    print('PYTHONHASHSEED=' + seed, '->', len(seen), 'order(s)')
