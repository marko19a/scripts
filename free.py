import re
import subprocess

file = open('/proc/meminfo', 'r')
lines = file.readlines()

total = float(re.search(r'\d+', lines[0]).group()) / (1024 * 1024)
av = float(re.search(r'\d+', lines[2]).group()) / (1024 * 1024)

subprocess.call(['notify-send', 'Memory', 'Available: %.2f (%d%s)' % (av, int(av/total*100), '%')])
