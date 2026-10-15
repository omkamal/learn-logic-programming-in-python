#!/usr/bin/env python3
r"""Run every example and check it against its recorded result.

    python tools/check_examples.py --all                 # every folder: ch01 ... ch17, appC, course
    python tools/check_examples.py ch04 ch05             # some chapters
    python tools/check_examples.py ch04/reach.py         # one file
    python tools/check_examples.py --all -j 8 --json report.json
    python tools/check_examples.py --all --repeat 2      # also run each file twice and list the ones whose output changes

Each chapter folder is copied to a temporary directory, so nothing is written next to the sources. For every runnable file
(*.py, and *.sql with the sqlite3 command line) the script compares

  * the exit code with  out/<name>.exit       (0 = normal; 124 = the example is a deliberate hang that the timeout stops)
  * the printed output with  out/<name>.out.txt

Verdicts: PASS (same exit code, same output) | PASS-ORDER (same exit code, the same output lines in a different order: answers
of a set have no fixed order) | PASS-VARIES (same exit code, different content, and the file is listed in nondeterministic.txt:
a demo whose numbers, ties or timings change on purpose) | DIFF (same exit code, different content: look at it) |
FAIL (different exit code) | SKIP (interpreter not installed) | SKIP-HEAVY (marked `heavy:` in its first lines, run only
with --heavy: ch16/estimate.py needs about 7 GB of memory). Exit status 0 only when nothing is DIFF or FAIL.
A file may start with a comment `# timeout: 15` (or `% timeout: 15`): the default limit is 60 seconds.
Environment used for every run: PYTHONHASHSEED=0, PYTHONWARNINGS=ignore::SyntaxWarning (a harmless warning that
pyDatalog 0.22.4 prints on Python 3.12).
"""
import argparse, concurrent.futures as cf, json, os, re, shutil, subprocess, sys, tempfile, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_ROOT = ROOT / "code" / "book" if (ROOT / "code" / "book").is_dir() else ROOT
RUNNABLE = {".py", ".sql"}


def interpreter(ext):
    if ext == ".py":
        return [sys.executable]
    if ext == ".sql":
        return ["sqlite3", ":memory:"] if shutil.which("sqlite3") else None
    return None


def command(path: Path):
    base = interpreter(path.suffix)
    if base is None:
        return None
    if path.suffix == ".sql":
        return base + [f".read {path.name}"]
    return base + [path.name]


def norm(text: str) -> str:
    """Make outputs comparable across machines: drop directory parts of file paths in tracebacks."""
    text = re.sub(r'File "[^"]*[/\\]([^/\\"]+)"', r'File ".../\1"', text)
    text = re.sub(r"(?:/[^\s\"':()]+)+/site-packages/", ".../site-packages/", text)
    text = re.sub(r"/home/[^/\s]+/", "~/", text)                                      # a home directory is not part of the result   # the library location differs per machine
    return text.replace("\r\n", "\n")


def run_file(path: Path, env):
    head = "\n".join(path.read_text(errors="replace").splitlines()[:3])
    m = re.search(r"timeout:\s*(\d+)", head)
    limit = int(m.group(1)) if m else 60
    cmd = command(path)
    if cmd is None:
        return None, "", 0.0
    t0 = time.time()
    try:
        r = subprocess.run(["timeout", "-k", "2", str(limit)] + cmd, cwd=path.parent, env=env,
                           capture_output=True, text=True, errors="replace")
        out, code = r.stdout + r.stderr, r.returncode
        if code in (124, 137):
            out += f"[killed after {limit} s: no answer, no error]\n"
            code = 124
    except FileNotFoundError as e:
        return None, f"[runner error: {e}]", 0.0
    return code, out, time.time() - t0


def check_chapter(src: Path, files, repeat, allow, heavy=False):
    results = []
    env = dict(os.environ, PYTHONHASHSEED="0", PYTHONWARNINGS="ignore::SyntaxWarning", PYTHONUNBUFFERED="1")
    with tempfile.TemporaryDirectory(prefix=f"examples-{src.name}-") as tmp:
        work = Path(tmp) / src.name
        shutil.copytree(src, work, ignore=shutil.ignore_patterns("__pycache__", "*.db", "*.sqlite"))   # out/ is copied: comparison scripts read it
        for f in files:
            p = work / f.name
            exp_out_f, exp_exit_f = src / "out" / f"{f.stem}.out.txt", src / "out" / f"{f.stem}.exit"
            exp_out = exp_out_f.read_text(errors="replace") if exp_out_f.exists() else None
            exp_exit = int(exp_exit_f.read_text().strip()) if exp_exit_f.exists() else None
            is_heavy = "heavy:" in "\n".join(f.read_text(errors="replace").splitlines()[:4])
            if is_heavy and not heavy:
                results.append({"file": f"{src.name}/{f.name}", "exit": None, "expected_exit": exp_exit, "seconds": 0.0, "verdict": "SKIP-HEAVY"})
                continue
            code, out, secs = run_file(p, env)
            rec = {"file": f"{src.name}/{f.name}", "exit": code, "expected_exit": exp_exit, "seconds": round(secs, 1)}
            if code is None:
                rec["verdict"] = "SKIP"
            elif exp_exit is None or exp_out is None:
                rec["verdict"] = "FAIL"; rec["why"] = "no recorded result in out/"
            elif code != exp_exit:
                rec["verdict"] = "FAIL"; rec["why"] = f"exit {code}, recorded {exp_exit}"; rec["tail"] = out.strip().splitlines()[-3:]
            elif norm(out) == norm(exp_out):
                rec["verdict"] = "PASS"
            elif sorted(norm(out).splitlines()) == sorted(norm(exp_out).splitlines()):
                rec["verdict"] = "PASS-ORDER"        # the same lines in a different order (set answers have no fixed order)
            elif rec["file"] in allow:
                rec["verdict"] = "PASS-VARIES"
            else:
                rec["verdict"] = "DIFF"
                a, b = norm(exp_out).splitlines(), norm(out).splitlines()
                rec["first_difference"] = next(((i + 1, x, y) for i, (x, y) in enumerate(zip(a, b)) if x != y),
                                               (min(len(a), len(b)) + 1, "", "(line count differs)"))
            if repeat > 1 and code is not None:
                outs = {norm(out)}
                for _ in range(repeat - 1):
                    outs.add(norm(run_file(p, env)[1]))
                rec["varies_in_order_only"] = len(outs) > 1 and len({tuple(sorted(o.splitlines())) for o in outs}) == 1
                rec["varies_between_runs"] = len({tuple(sorted(o.splitlines())) for o in outs}) > 1   # the content changes
            results.append(rec)
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="*", help="chNN folders or chNN/file.py")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--root", default=str(DEFAULT_ROOT), help="folder that holds the chNN folders")
    ap.add_argument("-j", type=int, default=6, help="chapters checked in parallel")
    ap.add_argument("--repeat", type=int, default=1, help="run each file this many times (>1 lists files whose output varies)")
    ap.add_argument("--heavy", action="store_true", help="also run the examples marked `heavy:` (ch16/estimate.py needs about 7 GB of memory)")
    ap.add_argument("--json", help="write the full report here")
    a = ap.parse_args()
    root = Path(a.root)
    allow_f = Path(__file__).resolve().parent / "nondeterministic.txt"
    allow = {l.strip() for l in allow_f.read_text().splitlines() if l.strip() and not l.startswith("#")} if allow_f.exists() else set()
    jobs = {}
    if a.all or not a.targets:
        for d in sorted(list(root.glob("ch*")) + list(root.glob("app*")) + list(root.glob("course"))):
            if d.is_dir():
                jobs[d] = sorted(f for f in d.iterdir() if f.suffix in RUNNABLE and not f.name.startswith("_"))
    for t in a.targets:
        p = root / t
        if p.is_dir():
            jobs[p] = sorted(f for f in p.iterdir() if f.suffix in RUNNABLE and not f.name.startswith("_"))
        elif p.is_file():
            jobs.setdefault(p.parent, []).append(p)
        else:
            print(f"not found: {t}"); return 2
    results = []
    with cf.ThreadPoolExecutor(max_workers=a.j) as ex:
        futs = {ex.submit(check_chapter, d, fs, a.repeat, allow, a.heavy): d for d, fs in jobs.items() if fs}
        for fu in cf.as_completed(futs):
            results += fu.result()
    results.sort(key=lambda r: r["file"])
    counts = {}
    for r in results:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    for r in results:
        if r["verdict"] in ("FAIL", "DIFF"):
            print(f"{r['verdict']}: {r['file']}: {r.get('why') or r.get('first_difference')}")
            for line in r.get("tail", []):
                print("      ", line)
        elif r["verdict"] == "SKIP":
            print(f"SKIP: {r['file']} (interpreter not installed)")
        elif r["verdict"] == "SKIP-HEAVY":
            print(f"SKIP-HEAVY: {r['file']} (needs a big machine: run it with --heavy)")
    if a.repeat > 1:
        print("content varies between runs:", ", ".join(r["file"] for r in results if r.get("varies_between_runs")) or "none")
        print("only the row order varies:  ", ", ".join(r["file"] for r in results if r.get("varies_in_order_only")) or "none")
    hangs = sum(1 for r in results if r["exit"] == 124 and r["expected_exit"] == 124)
    print(f"\n{len(results)} examples: " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())) +
          f"   ({hangs} deliberate hang{'s' if hangs != 1 else ''} stopped by the timeout)")
    if a.json:
        Path(a.json).write_text(json.dumps(results, indent=1))
    return 1 if counts.get("FAIL") or counts.get("DIFF") else 0


if __name__ == "__main__":
    sys.exit(main())
