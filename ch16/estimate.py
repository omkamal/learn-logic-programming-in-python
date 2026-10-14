# timeout: 240
import subprocess
import sys

US_PER_PAIR = 11.5          # about what growth_table.py measured
MB_PER_PAIR = 0.0015        # about 1.5 kilobytes per answer

def measure(shape, n):
    command = [sys.executable, '_growth_child.py', shape, str(n)]
    out = subprocess.run(command, capture_output=True, text=True).stdout
    name, links, pairs, seconds, peak = out.split()
    return int(links), int(pairs), float(seconds), int(peak)

n = 3000
guess = n * (n + 1) // 2
print('a chain of %d links: expect %d pairs, about %.0f s, about %.0f MB'
      % (n, guess, guess * US_PER_PAIR / 1e6, guess * MB_PER_PAIR))
links, pairs, seconds, peak = measure('chain', n)
print('measured:                 %d pairs, %.0f s, %d MB'
      % (pairs, seconds, peak))

# the same number of stops, but shaped like a tree
links, pairs, seconds, peak = measure('tree', n)
print('a tree of %d stops (%d links): %d pairs, %.2f s, %d MB'
      % (n, links, pairs, seconds, peak))
