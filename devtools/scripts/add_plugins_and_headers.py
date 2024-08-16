from delocate import wheeltools
from os.path import join
import os
import shutil
import sys

install_dir = sys.argv[1]
for filename in os.listdir('.'):
    #path = os.path.join('fixed', filename)
    with wheeltools.InWheel(filename, filename):
        shutil.copytree(join(install_dir, 'lib'), 'OpenMM.libs/lib')
        shutil.copytree(join(install_dir, 'include'), 'OpenMM.libs/include')