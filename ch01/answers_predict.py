# timeout: 60
# Three yes/no questions in plain Prolog, each with a 3-second limit.
import subprocess

SWIPL = "swipl"                    # found on the PATH

for goal in ["reach(cai, jfk)", "reach(jfk, cai)", "reach(cai, nrt)"]:
    cmd = [SWIPL, "-q", "-g", f"({goal} -> halt(0) ; halt(1))",
           "hang/flights_plain.pl"]
    try:
        run = subprocess.run(cmd, capture_output=True, timeout=3)
        code = run.returncode
        print(f"{goal:18s} {'yes' if code == 0 else 'no'}")
    except subprocess.TimeoutExpired:
        print(f"{goal:18s} no answer after 3 s (stopped)")
