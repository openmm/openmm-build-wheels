from delocate import wheeltools
from os.path import join
import os
import shutil
import sys

install_dir = sys.argv[1]
print('current dir:', os.getcwd())
for filename in os.listdir('fixed'):
    print('processing', filename)
    with wheeltools.InWheel(filename, filename):
        shutil.copytree(join(install_dir, 'lib', 'plugins'), 'OpenMM.libs/lib/plugins')
        shutil.copytree(join(install_dir, 'include'), 'OpenMM.libs/include')