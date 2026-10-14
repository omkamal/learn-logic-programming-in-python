# timeout: 20
# Run hang/reach_loop.pl (plain SWI-Prolog) with a 5-second limit.
from _limited import run_limited

SWIPL = "swipl"                    # found on the PATH
run_limited([SWIPL, "-q", "-g", "halt", "hang/reach_loop.pl"], 5)
