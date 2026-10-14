# Answer to exercise 2: policy.lp run with clingo, one atom per line.
import clingo

ctl = clingo.Control(["0", "--warn=none"])
ctl.load("policy.lp")
ctl.ground([("base", [])])

def show(model):
    for atom in sorted(str(a) for a in model.symbols(shown=True)):
        print(atom)

ctl.solve(on_model=show)
