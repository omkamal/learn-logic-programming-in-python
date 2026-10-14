# The staircase in plain Python: the same numbers, written out.
def climb(n):
    if n == 0:
        print('factorial[0] is a fact: 1')
        return 1
    print(f'factorial[{n}] needs factorial[{n - 1}]')
    below = climb(n - 1)
    answer = n * below
    print(f'factorial[{n}] = {n} * {below} = {answer}')
    return answer

climb(5)
