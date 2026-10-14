import subprocess
import sys

def run_with_timeout(script, seconds):
    """Run a script in its own process; give up after `seconds`."""
    try:
        done = subprocess.run([sys.executable, script], timeout=seconds,
                              capture_output=True, text=True)
    except subprocess.TimeoutExpired:
        return 'no answer and no error after %d s: killed' % seconds
    return (done.stdout + done.stderr).strip()

for script in ['pipes_first.py', 'pipes_last.py']:
    print(script, '->', run_with_timeout(script, 5))
