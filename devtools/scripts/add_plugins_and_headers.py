from delocate import wheeltools
from os.path import join
import os
import shutil
import sys

install_dir = sys.argv[1]
for filename in os.listdir('fixed'):
    path = os.path.join('fixed', filename)
    with wheeltools.InWheel(path, path):
        shutil.copytree(join(install_dir, 'lib'), 'OpenMM.libs/lib', dirs_exist_ok=True)
        shutil.copytree(join(install_dir, 'include'), 'OpenMM.libs/include', dirs_exist_ok=True)