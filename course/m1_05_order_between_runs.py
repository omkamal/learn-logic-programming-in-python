# The same tiny program in four fresh Python processes, each with its own hash seed
import os, subprocess, sys
program = """
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, parent')
+parent('alice', 'bob')
+parent('alice', 'carol')
print(parent('alice', X).data, sorted(parent('alice', X).data))
"""
for seed in ['1', '2', '3', '4']:
    env = dict(os.environ, PYTHONHASHSEED=seed, PYTHONWARNINGS='ignore')
    result = subprocess.run([sys.executable, '-c', program], env=env, capture_output=True, text=True)
    print('seed', seed, '->', result.stdout.strip())
