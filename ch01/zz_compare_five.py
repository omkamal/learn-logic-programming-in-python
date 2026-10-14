# Read the captured answers of five programs and compare them.
# (Run this one last: it needs the .out.txt files of the others.)
import ast
import re
from pathlib import Path

OUT = Path("out")

def words(text):
    return sorted(w.upper() for w in re.findall(r"[A-Za-z]+", text))

answers = {}
def read(name):
    return (OUT / f"{name}.out.txt").read_text()

rows = ast.literal_eval(read("pydatalog_reach").splitlines()[0])
answers["pyDatalog"] = sorted(r[0] for r in rows)
answers["SWI-Prolog, tabled"] = words(read("reach_tabled"))
answers["SQLite CTE"] = words(read("cte_union"))
answers["clingo"] = words(read("reach_from_cai").replace("Answer:", ""))
third_line = read("z3_fixedpoint").splitlines()[2]
answers["Z3 Fixedpoint"] = words(third_line.split(":")[1])

for tool, cities in answers.items():
    print(f"{tool:20s} {cities}")
print("all five agree:", len({tuple(v) for v in answers.values()}) == 1)
