# PyDatalog Cookbook

Runnable examples for [pyDatalog](https://pypi.org/project/pyDatalog/): logic programming in Python. Every example is a small, complete file
that you can run, and the output it printed when it was recorded sits next to it. The examples are the companion code of the book
*Logic Programming in Python with PyDatalog: A Gentle, Illustrated Guide* (in preparation) and of the four-video course of the same name.

## Quick start

```bash
git clone https://github.com/omkamal/pydatalog-cookbook.git
cd pydatalog-cookbook
uv sync                                        # Python 3.12 with pyDatalog 0.22.4, SQLAlchemy 2.1.4, z3-solver, clingo
uv run python ch04/ancestor.py                 # run one example
uv run python tools/check_examples.py --all    # run every example and check it against its recorded result
```

You do not have to use `uv`: any Python 3.12 or 3.13 environment with the four packages in `pyproject.toml` works.
On Python 3.12 the first import of pyDatalog prints a harmless `SyntaxWarning` (a regular expression in the library); the verifier silences it.
Two folders also need tools that are not Python packages: `ch01` and `ch17` call **SWI-Prolog** (`swipl` on the PATH; for example
`conda install -c conda-forge swi-prolog`), and `ch01` and `ch08` call the **`sqlite3`** command line. Without them the `.pl` examples are reported as `SKIP` and the three Python examples that start `swipl` (`ch01/reach_loop_run.py`, `ch01/answers_predict.py`, `ch17/ring_engines.py`) fail.

## What is in each folder

| folder | topic | examples |
|---|---|---|
| `appC/` | Appendix C: every error message and silent failure of the book, reproduced one by one | 89 |
| `ch01/` | A Short History of Asking Computers Questions | 25 |
| `ch02/` | Setting Up and Stating Facts | 31 |
| `ch03/` | Rules: Teaching the Computer to Infer | 31 |
| `ch04/` | Recursion, Gently | 26 |
| `ch05/` | Loops and the Order of Things | 25 |
| `ch06/` | Saying “Not” | 21 |
| `ch07/` | Computing Inside Rules | 39 |
| `ch08/` | Aggregates: From Many to One | 27 |
| `ch09/` | Ranking, Running Totals and Shortest Paths | 32 |
| `ch10/` | Logic Meets Python Objects | 30 |
| `ch11/` | Python Functions Inside Logic | 34 |
| `ch12/` | Talking to SQL Databases | 25 |
| `ch13/` | Capstone: Who May Do What | 22 |
| `ch14/` | Capstone: Parts, Teams and Dependencies | 33 |
| `ch15/` | Puzzles: The N-Queens Problem | 25 |
| `ch16/` | Speed, Limits and Debugging | 23 |
| `ch17/` | Choosing Your Tool | 16 |
| `course/` | The 44 snippets of the four-video course (modules 1 to 4) | 44 |

Each folder has an `out/` subfolder with `name.out.txt` (the recorded output) and `name.exit` (the recorded exit code) for every example.

## Checking the examples

`tools/check_examples.py` copies each folder to a temporary directory, runs every example there with `PYTHONHASHSEED=0`, and compares the exit code
and the printed output with the recorded ones. Verdicts: `PASS`, `PASS-ORDER` (the same lines in another order: answers of a set have no fixed order),
`PASS-VARIES` (listed in `tools/nondeterministic.txt`), `DIFF`, `FAIL` and `SKIP`. The exit status is non-zero only for `DIFF` and `FAIL`.

* **24 examples are deliberate hangs.** They show what a program that never finishes looks like; a timeout stops them, the recorded exit code is 124
  and the last recorded line reads `[killed after N s: no answer, no error]`. A header such as `# timeout: 10` on the first lines sets the limit.
* **30 examples change from run to run on purpose** (answer order inside a line, ties, memory sizes, timings). They are listed in `tools/nondeterministic.txt`,
  and for them only the exit code is compared. All other examples print the same text every time.
* Timings in the recorded outputs come from one machine (Intel Core i7-14700K, Linux). Expect other numbers on yours.

## How these were checked

All 598 examples were run from a fresh `uv sync` of this repository and passed `tools/check_examples.py --all`
(Python 3.12.3, pyDatalog 0.22.4, SQLAlchemy 2.1.4, z3-solver 5.1.0.0, clingo 5.8.2, SWI-Prolog 10.0.0).
Setup-diagnostic scripts that print the versions of one particular machine, and outputs that were captured by hand rather than by a script, are not included.
