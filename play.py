import sys
import subprocess
import re

if len(sys.argv) == 1:
    file = open('/home/marko/.play', 'r')
    line = file.readline()
    x = re.search('E\d\d', line)
    x = x.span()[0] + 1
    ep = line[x:x+2]
    iep = int(ep) + 1

    line = list(line)
    file.close()
    file = open('/home/marko/.play', 'w')
    if iep <= 9:
        line[x] = '0'
        line[x+1] = f'{iep}'
        line = ''.join(line)
    else:
        line[x] = f'{iep}'
        line[x + 1] = ''
        line = ''.join(line)

    file.write(line)
    file.close()

    subprocess.call(['mplayer', line])

else:
    if sys.argv[1] == 'r':
        file = open('/home/marko/.play')
        line = file.readline()
        file.close()

        subprocess.call(['mplayer', line])
    else:
        file = open('/home/marko/.play', 'w')
        file.write(sys.argv[1])
        file.close()

        subprocess.call(['mplayer', sys.argv[1]])
