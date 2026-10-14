told = [('mia', 'noor'), ('mia', 'omar'), ('noor', 'pat'),
        ('omar', 'quinn'), ('pat', 'ravi'), ('quinn', 'sam'),
        ('tess', 'pat')]

heard = set()                    # everyone who has heard it so far
ring = {'mia'}                   # the people the rumor just reached
n = 0
while ring:
    n += 1
    ring = {b for (a, b) in told if a in ring} - heard
    print(f'round {n}:', ' '.join(sorted(ring)) or 'nobody new, stop')
    heard |= ring
