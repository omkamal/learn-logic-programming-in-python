import clingo

ctl = clingo.Control(['0'])
try:
    ctl.add('base', [], 'p :- q')       # no full stop at the end
    ctl.ground([('base', [])])
except RuntimeError as err:
    print(type(err).__name__ + ':', err)
