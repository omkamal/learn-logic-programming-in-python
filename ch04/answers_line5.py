# Answer to question 1: a line of five people, the notebook by rounds
people = ['a', 'b', 'c', 'd', 'e']
parent = list(zip(people, people[1:]))        # a-b, b-c, c-d, d-e

notebook = set(parent)
print('round 1:', len(notebook), 'new')
n = 1
while True:
    n += 1
    new = {(x, y) for (x, z) in notebook
                  for (z2, y) in parent if z == z2} - notebook
    print(f'round {n}:', len(new), 'new', sorted(new)[:1] if new
          else '(stop)')
    if not new:
        break
    notebook |= new

print('total:', len(notebook), 'cards;', ('a', 'e') in notebook)
