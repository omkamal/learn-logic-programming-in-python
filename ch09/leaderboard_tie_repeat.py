import subprocess
import sys
from collections import Counter


def answers(script, times=12):
    seen = Counter()
    for _ in range(times):
        run = subprocess.run([sys.executable, script],
                             capture_output=True, text=True)
        seen[run.stdout.strip()] += 1
    return seen


for script in ('leaderboard_tie.py', 'leaderboard_tiebreak.py'):
    print(script)
    for answer, count in sorted(answers(script).items()):
        print(' ', count, 'x', answer)
