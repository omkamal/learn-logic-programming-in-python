# Learn Logic Programming in Python: companion code

The runnable examples of the book *Learn Logic Programming in Python: A Gentle, Illustrated Guide with PyDatalog, from Facts and Rules to Recursion, SQL and Real Applications*
by Omar Kamal Hosney, and of a four-video course on pyDatalog (the library: [pypi.org/project/pyDatalog](https://pypi.org/project/pyDatalog/)). The book teaches you to think in facts, rules and queries, using
pyDatalog inside ordinary Python. Every example is a small, complete file that you can run, and the output it printed when it was recorded sits next to it.

## Quick start

```bash
git clone https://github.com/omkamal/learn-logic-programming-in-python.git
cd learn-logic-programming-in-python
uv sync                                        # Python 3.12 with pyDatalog 0.22.4 and SQLAlchemy 2.1.4
uv run python ch01/grandparent_rule.py         # run one example (the grandparent rule of Chapter 1)
uv run python tools/check_examples.py ch04     # run one chapter's examples and check them against their recorded results
```

**License.** The code in this repository is released under the [MIT License](LICENSE). The text and illustrations of the book are not part of it.

Install [uv](https://docs.astral.sh/uv/) first (Appendix A of the book shows how). Start with the chapter you are reading. Running **everything** (`--all`) takes a good while on a laptop: about 560 examples, 21 of them deliberately left running until a timeout stops them (see below).

You do not have to use `uv`: any Python 3.12 or 3.13 environment with the two packages in `pyproject.toml` works. The outputs were recorded on **Python 3.12.3** (a `.python-version` file asks `uv` for 3.12); on 3.13 two examples (`ch08/arg_errors.py`, `appC/err_agg_python_sum.py`) differ only in the wording of a Python error message.
On Python 3.12 and 3.13 the first import of pyDatalog prints a harmless `SyntaxWarning` (a regular expression in the library); the checker silences it.

Things the examples need besides Python:

* The 3 `.sql` examples in `ch08` use the **`sqlite3`** command line; without it they are reported as `SKIP`.
* Two examples (`ch02/uv_setup.py`, `course/m1_07_uv_setup.py`) run `uv` itself and download pyDatalog, so they need `uv` and an internet connection.
* Five examples read a data file or a helper next to them, so run them from inside their folder: `cd ch11 && uv run python load_files.py` (also `receipt.py`, `load_trap.py`), and `cd ch16 && uv run python growth_table.py` (also `estimate.py`). The checker does this for you.
* Everything was written and checked on **Linux**. The checker needs the GNU `timeout` command, and six examples use Unix-only modules (`ch05/stopwatch.py`, `ch05/watch_hang.py`, `ch16/growth_table.py`, `ch16/estimate.py`, `course/m2_05_hang_timeout.py`, `course/m4_08_scaling.py`); on Windows use WSL.

## What is in each folder

| folder | topic | examples |
|---|---|---|
| `appC/` | Appendix C: every error message and silent failure of the book, reproduced one by one (plus `cheat_forms.py`, the run of Appendix B) | 85 |
| `ch01/` | What Is Logic Programming? | 3 |
| `ch02/` | Setting Up and Stating Facts | 31 |
| `ch03/` | Rules: Teaching the Computer to Infer | 31 |
| `ch04/` | Recursion, Gently | 26 |
| `ch05/` | Loops and the Order of Things | 27 |
| `ch06/` | Saying “Not” | 21 |
| `ch07/` | Computing Inside Rules | 39 |
| `ch08/` | Aggregates: From Many to One | 28 |
| `ch09/` | Ranking, Running Totals and Shortest Paths | 32 |
| `ch10/` | Logic Meets Python Objects | 30 |
| `ch11/` | Python Functions Inside Logic | 34 |
| `ch12/` | Talking to SQL Databases | 25 |
| `ch13/` | Capstone: Who May Do What | 22 |
| `ch14/` | Capstone: Parts, Teams and Dependencies | 33 |
| `ch15/` | Puzzles: The N-Queens Problem | 25 |
| `ch16/` | Speed, Limits and Debugging | 23 |
| `course/` | The 45 snippets of the four-video course on pyDatalog (modules 1 to 4); the book does not include them | 45 |

Each folder has an `out/` subfolder with `name.out.txt` (the recorded output) and `name.exit` (the recorded exit code) for every example.
The folder numbers are the chapter numbers of the book (Chapter 17 has no code), and the file name printed above each code block of the book is the path of the file in this repository, with two exceptions: the setup files of Appendix A (the `pyproject.toml` and `uv.lock` in the root are the project files shown there) and three hand-captured runs, `ch16/out/py_check_*.txt`, which appear only in the book together with the helper `ch16/_py_check.py`. `ch04/agreement_check.py` and `ch15/agree_check.py` are extras that the book does not show.

## One heavy example

> **Warning.** `ch16/estimate.py` builds 4.5 million answers on purpose, to show how fast answers grow. On the machine used for the recorded run it needed about **6.8 GB of memory** and about **54 seconds**. On a small laptop it can slow the whole machine down or be killed. The file says so in its first lines (the word `heavy:`), and `tools/check_examples.py` **skips it unless you pass `--heavy`**:
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
  and for them only the exit code is compared. Examples that print the answers of a set can list the rows in another order from one run to the next (the checker then says `PASS-ORDER`); the book sorts such answers on purpose.
* Timings in the recorded outputs come from one machine (Intel Core i7-14700K, Linux). Expect other numbers on yours.

## How these were checked

All 560 examples were run from a fresh `uv sync` of this repository and passed `tools/check_examples.py --all --heavy`
(Python 3.12.3, pyDatalog 0.22.4, SQLAlchemy 2.1.4, SQLite 3.49.1).
Setup-diagnostic scripts that print the versions of one particular machine, and outputs that were captured by hand rather than by a script, are not included.
