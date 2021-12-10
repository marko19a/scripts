import os
import re
import sys
import subprocess
import pathlib

player = 'mplayer'
play_file = f'{pathlib.Path.home()}/.play'
filetypes = (
    '265 26l 3ga 3gp 3p2 4xm aac asf avi buk cpk dat ' +
    'h264 ifv kmv m2t mj2 mjp mjp2 mk3d mka mkv mov mp3 mp4 ' +
    'mpeg mpg4 mqv nut ogg ogm qt rm roq smi ssa ts vc1 vivo ' +
    'vob vp3 vro webm wma wmv'
).split(' ')

def isVid(file):
    for type in filetypes:
        if type in file:
            return True

    return False

if len(sys.argv) == 1:
    with open(play_file, 'r') as f:
        line = f.readline()

    x = re.search('E|e\d\d', line)
    x = x.span()[0] + 1
    ep = int(line[x:x+2]) + 1

    parent = pathlib.Path(line).parent
    eps = os.listdir(parent)
    eps = list(filter(isVid, eps))
    eps.sort(key=lambda x: x.upper())
    
    if ep-1 >= len(eps):
        print(f'No more eps last is {ep-1:02d}')
        exit()

    next = f'{parent}/{eps[ep-1]}'
    with open(play_file, 'w') as f:
        f.write(next)

    subprocess.call([player, next])

else:
    if sys.argv[1] == 'r':
        with open(play_file, 'r') as f:
            line = f.readline()

        subprocess.call([player, line])
    else:
        with open(play_file, 'w') as f:
            fpath = pathlib.Path(sys.argv[1]).absolute().__str__()
            print(fpath)
            f.write(fpath)

        subprocess.call([player, sys.argv[1]])
