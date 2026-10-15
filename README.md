# Learn Logic Programming in Python: companion code

The runnable examples of the book *Learn Logic Programming in Python: A Gentle, Illustrated Guide with PyDatalog, from Facts and Rules to Recursion, SQL and Real Applications*
by Omar Kamal Hosney, and of the four-video course on [pyDatalog](https://pypi.org/project/pyDatalog/). The book teaches you to think in facts, rules and queries, using
pyDatalog inside ordinary Python. Every example is a small, complete file that you can run, and the output it printed when it was recorded sits next to it.

## Quick start

```bash
git clone https://github.com/omkamal/learn-logic-programming-in-python.git
cd learn-logic-programming-in-python
uv sync                                        # Python 3.12 with pyDatalog 0.22.4 and SQLAlchemy 2.1.4
uv run python ch04/ancestor.py                 # run one example
uv run python tools/check_examples.py ch04     # run one chapter's examples and check them against their recorded results
```

Start with a single chapter such as `ch04`. Running **everything** (`--all`) takes a good while on a laptop: about 559 examples, 21 of them deliberately left running until a timeout stops them (see below).

You do not have to use `uv`: any Python 3.12 or 3.13 environment with the two packages in `pyproject.toml` works.
On Python 3.12 the first import of pyDatalog prints a harmless `SyntaxWarning` (a regular expression in the library); the verifier silences it.
One example in `ch08` uses the **`sqlite3`** command line; without it that example is reported as `SKIP`.

## What is in each folder

| folder | topic | examples |
|---|---|---|
| `appC/` | Appendix C: every error message and silent failure of the book, reproduced one by one | 85 |
| `ch01/` | What Is Logic Programming? | 3 |
| `ch02/` | Setting Up and Stating Facts | 31 |
| `ch03/` | Rules: Teaching the Computer to Infer | 31 |
| `ch04/` | Recursion, Gently | 26 |
| `ch05/` | Loops and the Order of Things | 27 |
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
| `course/` | The 45 snippets of the four-video course (modules 1 to 4) | 45 |

Each folder has an `out/` subfolder with `name.out.txt` (the recorded output) and `name.exit` (the recorded exit code) for every example.
The folder numbers are the chapter numbers of the book, and the file name printed above each code block of the book is the path of the file in this repository.

## One heavy example

> **Warning.** `ch16/estimate.py` builds 4.5 million answers on purpose, to show how fast answers grow. On the machine used for the recorded run it needed about **6.8 GB of memory** and about **54 seconds**. On a small laptop it can slow the whole machine down or be killed. The file says so in its first lines (`# heavy:`), and `tools/check_examples.py` **skips it unless you pass `--heavy`**:
>
> ```bash
> uv run python tools/check_examples.py --all            # skips the heavy example (reported as SKIP-HEAVY)
> uv run python tools/check_examples.py --all --heavy    # includes it: only on a machine with enough free memory
> ```

## Checking the examples

`tools/check_examples.py` copies each folder to a temporary directory, runs every example there with `PYTHONHASHSEED=0`, and compares the exit code
and the printed output with the recorded ones. Verdicts: `PASS`, `PASS-ORDER` (the same lines in another order: answers of a set have no fixed order),
`PASS-VARIES` (listed in `tools/nondeterministic.txt`), `DIFF`, `FAIL`, `SKIP` (a tool is missing) and `SKIP-HEAVY` (see above). The exit status is non-zero only for `DIFF` and `FAIL`.

* **21 examples are deliberate hangs.** They show what a program that never finishes looks like; a timeout stops them, the recorded exit code is 124
  and the last recorded line reads `[killed after N s: no answer, no error]`. A header such as `# timeout: 10` on the first lines sets the limit.
* **25 examples change from run to run on purpose** (answer order inside a line, ties, memory sizes, timings). They are listed in `tools/nondeterministic.txt`,
  and for them only the exit code is compared. All other examples print the same text every time.
* Timings in the recorded outputs come from one machine (Intel Core i7-14700K, Linux). Expect other numbers on yours.

## How these were checked

All 559 examples were run from a fresh `uv sync` of this repository and passed `tools/check_examples.py --all --heavy`
(Python 3.12.3, pyDatalog 0.22.4, SQLAlchemy 2.1.4, SQLite 3.49.1).
Setup-diagnostic scripts that print the versions of one particular machine, and outputs that were captured by hand rather than by a script, are not included.
