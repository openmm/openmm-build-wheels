from delocate import wheeltools
from os.path import join, isdir
import os
import shutil
import sys

install_dir = sys.argv[1]
if len(sys.argv) == 2:
    ignore = None
else:
    platforms = sys.argv[2:]
    def ignore(dir, files):
        print("platforms:", platforms)
        ignore = []
        for platform in platforms:
            if platform[0] == '!':
                ignore += [f for f in files if platform[1:] in f]
            else:
                ignore += [f for f in files if platform not in f and not isdir(join(dir, f))]
        print("ignore:", ignore)
        return ignore
for filename in os.listdir('.'):
    if filename.endswith('.whl'):
        with wheeltools.InWheel(filename, filename):
            shutil.copytree(join(install_dir, 'lib'), 'OpenMM.libs/lib', dirs_exist_ok=True, ignore=ignore)
            shutil.copytree(join(install_dir, 'include'), 'OpenMM.libs/include', dirs_exist_ok=True)