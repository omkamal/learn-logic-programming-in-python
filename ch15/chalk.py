import time

# The explorer of the chapter, written out in plain Python. We write it
# to count and time its steps: the pyDatalog programs contain none of it.

def safe(cols, k):
    """Is the queen just placed in row k safe from the rows above?"""
    return all(cols[i] != cols[k] and abs(cols[i] - cols[k]) != k - i
               for i in range(k))

def explore(n):
    safe_boards = [0] * (n + 1)   # safe boards with 0, 1, ... n queens
    tries = 0
    solutions = []

    def walk(cols):
        nonlocal tries
        safe_boards[len(cols)] += 1
        if len(cols) == n:
            solutions.append(tuple(cols))
            return
        for c in range(n):
            tries += 1                    # one more chalk mark
            cols.append(c)
            if safe(cols, len(cols) - 1):
                walk(cols)                # go deeper
            cols.pop()                    # rub the mark out

    walk([])
    return safe_boards, tries, solutions

for n in (4, 8):
    start = time.perf_counter()
    boards, tries, solutions = explore(n)
    seconds = time.perf_counter() - start
    print(n, 'queens: safe boards per row', boards)
    print('   tries', tries, 'against', n ** n, 'column lists')
    print('   solutions', len(solutions), 'first', solutions[0])
    print('   plain Python took', round(seconds * 1000, 1), 'ms')
