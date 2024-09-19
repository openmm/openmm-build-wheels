from delocate import wheeltools
from os.path import join
import os
import shutil
import sys

install_dir = sys.argv[1]
if len(sys.argv) == 2:
    ignore = None
elif sys.argv[2][0] == '!':
    platform = sys.argv[2][1:]
    def ignore(dir, files):
        return [f for f in files if platform in f]
else:
    platform = sys.argv[2]
    def ignore(dir, files):
        return [f for f in files if platform not in f]
for filename in os.listdir('.'):
    if filename.endswith('.whl'):
        with wheeltools.InWheel(filename, filename):
            shutil.copytree(join(install_dir, 'lib'), 'OpenMM.libs/lib', dirs_exist_ok=True, ignore=ignore)
            shutil.copytree(join(install_dir, 'include'), 'OpenMM.libs/include', dirs_exist_ok=True)