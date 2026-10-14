# timeout: 40
# The same loop without an exit: this time Prolog stops with a message.
import subprocess

run = subprocess.run(['swipl', '-q', '-g', 'halt', '_reach_cycle.pl'],
                     capture_output=True, text=True, timeout=30)
for line in (run.stdout + run.stderr).splitlines():
    if 'Stack limit' in line:
        print(line.strip())
