import multiprocessing
from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, flight, reach')

def run(n, order, answers):
    names = 'ABCDEFGH'[:n]
    for i in range(n):
        +flight(names[i], names[(i + 1) % n])   # a loop of n airports
    reach(X, Y) <= flight(X, Y)
    if order == 'FIRST':
        reach(X, Y) <= reach(X, Z) & flight(Z, Y)
    else:
        reach(X, Y) <= flight(X, Z) & reach(Z, Y)
    answers.value = len(reach('A', Y).data)

if __name__ == '__main__':
    for n in range(1, 7):
        row = []
        for order in ('FIRST', 'LAST'):
            answers = multiprocessing.Value('i', -1)
            child = multiprocessing.Process(target=run, args=(n, order, answers))
            child.start()
            child.join(timeout=5)                  # wait at most 5 seconds
            if child.is_alive():
                child.kill()
                child.join()
                row.append(f'{order}: no answer after 5 s')
            elif answers.value > 0:
                row.append(f'{order}: finished')
            else:
                row.append(f'{order}: ended with no answers')
        print(f'loop of {n}:', ' | '.join(row), flush=True)
