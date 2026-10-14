"""Run a command with a time limit and print what it printed.

tools/run_code.py cannot record the killed run of a looping SWI-Prolog
program: swipl ignores SIGTERM inside this loop, and `timeout -k` then
kills its own process group, so the runner sees exit -9 and writes no
"[killed ...]" line. This helper does the stopping itself (SIGKILL after
the limit) and prints the same last line that run_code.py would print.
"""
import subprocess
import sys


def run_limited(cmd, seconds):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=seconds)
        sys.stdout.write(r.stdout + r.stderr)
    except subprocess.TimeoutExpired as e:
        for part in (e.stdout, e.stderr):
            if part:
                sys.stdout.write(part.decode() if isinstance(part, bytes)
                                 else part)
        print(f"[killed after {seconds} s: no answer, no error]")
