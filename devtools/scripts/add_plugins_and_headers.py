from delocate import wheeltools
from os.path import join
import os
import shutil
import sys

install_dir = sys.argv[1]
for filename in os.listdir('fixed'):
    with wheeltools.InWheel(filename, filename):
        shutil.copytree(join(install_dir, 'lib', 'plugins'), 'OpenMM.libs/lib/plugins')
        shutil.copytree(join(install_dir, 'include'), 'OpenMM.libs/include')