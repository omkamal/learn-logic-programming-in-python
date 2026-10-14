# timeout: 20
# swipl ignores a polite stop inside this loop, so stop it ourselves.
import subprocess

try:
    subprocess.run(['swipl', '-q', '-g', 'halt', '_reach_loop.pl'],
                   capture_output=True, text=True, timeout=5)
except subprocess.TimeoutExpired:
    print('[killed after 5 s: no answer, no error]')
