# What the very first import prints, and what later imports print
import os, subprocess, sys, tempfile
cmd = [sys.executable, '-c', 'from pyDatalog import pyDatalog']
base = {k: v for k, v in os.environ.items() if k != 'PYTHONWARNINGS'}

def run(label, **extra):
    err = subprocess.run(cmd, env=dict(base, **extra), capture_output=True, text=True).stderr
    print(f'--- {label}: {len(err.splitlines())} line(s) on stderr')
    print(err, end='')

with tempfile.TemporaryDirectory() as cache:   # an empty bytecode cache = a first import
    run('first import', PYTHONPYCACHEPREFIX=cache)
    run('second import', PYTHONPYCACHEPREFIX=cache)
with tempfile.TemporaryDirectory() as cache:
    run('first import with PYTHONWARNINGS=ignore', PYTHONPYCACHEPREFIX=cache, PYTHONWARNINGS='ignore')
