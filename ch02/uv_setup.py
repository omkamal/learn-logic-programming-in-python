# A fresh uv project with pyDatalog 0.22.4, captured for real
import os, re, shlex, shutil, subprocess
from pathlib import Path
env = {k: v for k, v in os.environ.items()
       if k not in ('VIRTUAL_ENV', 'PYTHONWARNINGS')}
root = Path('/tmp/pydl-ch02-demo')
shutil.rmtree(root, ignore_errors=True)
root.mkdir()
project = root / 'family-tree'
hello = ('from pyDatalog import pyDatalog\n'
         'print("pyDatalog imported")\n')


def tidy(text):  # shorten two long paths for the page, nothing else
    text = re.sub(r'interpreter at: .*', 'interpreter at: <python3.12>',
                  text)
    return text.replace(str(project) + '/.venv/lib/python3.12/'
                        'site-packages/', '')


def run(cwd, *cmd):
    print('$', shlex.join(cmd))
    done = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True,
                          text=True)
    print(tidy(done.stderr + done.stdout).rstrip())


run(root, 'uv', 'init', '--python', '3.12', '--vcs', 'none',
    'family-tree')
run(project, 'uv', 'add', 'pyDatalog==0.22.4')
print('$ ls -A')
print(' '.join(sorted(os.listdir(project))))
(project / 'hello.py').write_text(hello)
run(project, 'uv', 'run', 'python', 'hello.py')
run(project, 'uv', 'run', 'python', 'hello.py')
run(project, 'uv', 'sync')
shutil.rmtree(root)
