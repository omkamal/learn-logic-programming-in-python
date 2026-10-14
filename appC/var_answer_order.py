# timeout: 60
# Start the same tiny program 16 times in fresh processes, same hash seed.
import subprocess
import sys

child = """
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, parent')
+parent('alice', 'bob')
+parent('alice', 'carol')
q = parent('alice', X)
print(q.data)
print(sorted(q.data))
"""
raw, tidy = set(), set()
for _ in range(16):
    out = subprocess.run([sys.executable, '-c', child],
                         capture_output=True, text=True).stdout
    first, second = out.splitlines()
    raw.add(first)
    tidy.add(second)

print('different raw orders seen:   ', len(raw))
print('different sorted orders seen:', len(tidy))
print(sorted(tidy))
