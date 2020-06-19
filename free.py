import re
import subprocess

file = open('/proc/meminfo', 'r')
lines = file.readlines()

total = float(re.search(r'\d+', lines[0]).group()) / (1024 * 1024)
av = float(re.search(r'\d+', lines[2]).group()) / (1024 * 1024)

file.close()
file = open('/proc/cpuinfo')
lines = file.readlines()

mhz = float(re.search(r'\d+', lines[7]).group())
'''
file.close()
file = open('/proc/stat')
line = file.readline()

values = re.findall(r'\d+', line)

values = [int(v) for v in values]

p = (values[3] * 20) / (sum(values[:3]) + sum(values[4:]))
'''
file.close()
subprocess.call(
    ['notify-send', 'Memory', 'MEM: %.2f (%d%s) | CPU: %d MHz' % (av, int(av / total * 100), '%', mhz)])
