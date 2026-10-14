# A fresh uv project with pyDatalog 0.22.4, captured for real
import os, shlex, shutil, subprocess, tempfile
from pathlib import Path
env = {k: v for k, v in os.environ.items() if k not in ('VIRTUAL_ENV', 'PYTHONWARNINGS')}
root = Path(tempfile.mkdtemp(prefix='uv-demo-'))
project = root / 'family-tree'
steps = [
    (root, ['uv', 'init', '--python', '3.12', '--vcs', 'none', 'family-tree']),
    (project, ['uv', 'add', 'pyDatalog==0.22.4']),
    (project, ['uv', 'run', 'python', '-c', 'from pyDatalog import pyDatalog; print("pyDatalog imported")']),
]
for cwd, cmd in steps:
    print('$', shlex.join(cmd))
    result = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)
    print((result.stderr + result.stdout).rstrip())
print('$ cat pyproject.toml')
print((project / 'pyproject.toml').read_text().rstrip())
shutil.rmtree(root)
