# What the very first import prints, and what later imports print
import os, subprocess, sys, tempfile
cmd = [sys.executable, '-c', 'from pyDatalog import pyDatalog']
base = {k: v for k, v in os.environ.items() if k != 'PYTHONWARNINGS'}


def run(label, **extra):
    env = dict(base, **extra)
    err = subprocess.run(cmd, env=env, capture_output=True,
                         text=True).stderr
    print('---', label + ':', len(err.splitlines()), 'line(s) on stderr')


with tempfile.TemporaryDirectory() as cache:   # empty cache = first import
    run('first import', PYTHONPYCACHEPREFIX=cache)
    run('second import', PYTHONPYCACHEPREFIX=cache)
with tempfile.TemporaryDirectory() as cache:
    run('first import, PYTHONWARNINGS=ignore', PYTHONPYCACHEPREFIX=cache,
        PYTHONWARNINGS='ignore')
