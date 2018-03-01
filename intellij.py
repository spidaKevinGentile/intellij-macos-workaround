#!/usr/bin/env python3
import subprocess
cmd = "open"
arg = "-a"
prog = "intelliJ IDEA CE"
print('opening '+prog+'...')
subprocess.Popen([cmd, arg, prog])

