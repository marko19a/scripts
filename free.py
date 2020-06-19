import re
import os
import subprocess

file = open('/proc/meminfo', 'r')
lines = file.readlines()

total = float(re.search(r'\d+', lines[0]).group()) / (1024 * 1024)
av = float(re.search(r'\d+', lines[2]).group()) / (1024 * 1024)

file.close()
file = open('/proc/cpuinfo')
lines = file.readlines()

mhz = float(re.search(r'\d+', lines[7]).group())

CPU_Pct = str(round(
    float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),
    2))

file.close()
subprocess.call(
    ['notify-send', 'Memory',
     'M: %.2f (%d%s) | C: %d MHz' % (av, int(av / total * 100), '%', mhz)])
