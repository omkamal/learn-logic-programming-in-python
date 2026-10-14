# timeout: 90
# The same program, 12 fresh processes, 4 seconds each.
import subprocess
import sys

child = """
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, move, win')
+move('a', 'b')
+move('b', 'a')
+move('b', 'c')
win(X) <= move(X, Y) & ~win(Y)
print(sorted(win(X).data))
"""
outcomes = []
for _ in range(12):
    try:
        out = subprocess.run([sys.executable, '-c', child], timeout=4,
                             capture_output=True, text=True).stdout
        outcomes.append(out.strip())
    except subprocess.TimeoutExpired:
        outcomes.append('no answer in 4 s')

print('different outcomes seen:', len(set(outcomes)))
print(sorted(set(outcomes)))
