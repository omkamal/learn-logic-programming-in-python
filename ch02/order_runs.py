# timeout: 90
# The same tiny program in fresh Python processes, to watch the order
import os, subprocess, sys
cards = [('alice', 'bob'), ('alice', 'carol'),
         ('bob', 'dave'), ('carol', 'erin')]
program = """
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, parent')
""" + ''.join(f'+parent{card}\n' for card in cards) + """
print(parent('alice', X).data, sorted(parent('alice', X).data))
print(parent(X, Y).data)
"""


def run(seed):
    env = dict(os.environ, PYTHONHASHSEED=seed, PYTHONWARNINGS='ignore')
    done = subprocess.run([sys.executable, '-c', program], env=env,
                          capture_output=True, text=True)
    return done.stdout.strip().splitlines()


seen = set()
for seed in range(1, 13):          # new seed each time, stop at a change
    line = run(str(seed))[0]
    print('seed', seed, '->', line)
    seen.add(line)
    if len(seen) == 2:
        break

same = [run('0') for _ in range(20)]
for k, label in [(0, "parent('alice', X)"), (1, 'parent(X, Y)')]:
    kinds = len({lines[k] for lines in same})
    print('20 runs, seed 0,', label + ':', kinds, 'different raw order(s)')
backwards = str(list(reversed(cards)))
print('every-card order = typing order reversed:',
      all(lines[1] == backwards for lines in same))
