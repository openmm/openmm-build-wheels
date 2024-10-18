from delocate import wheeltools, tools
from os.path import join
import os
import sys

install_dir = sys.argv[1]
for wheelname in os.listdir(install_dir):
    if wheelname.endswith('.whl'):
        with wheeltools.InWheel(wheelname, wheelname):
            for libname in os.listdir('openmm'):
                if libname.endswith('.so'):
                    tools._delete_rpaths(join('openmm', libname), ['/Users/runner/openmm-install/lib'])
                    tools.add_rpath(join('openmm', libname), '../OpenMM.libs/lib')
