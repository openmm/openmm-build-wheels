from delocate import wheeltools, tools
from os.path import join
import os
import sys

install_dir = sys.argv[1]
for wheelname in os.listdir(install_dir):
    if wheelname.endswith('.whl'):
        print('wheel name', wheelname)
        with wheeltools.InWheel(wheelname, wheelname):
            for libname in os.listdir('openmm'):
                if libname.endswith('.so'):
                    print('lib name', libname)
                    print('current rpaths:', tools.get_rpaths(join('openmm', libname)))
                    tools._delete_rpaths(join('openmm', libname), ['/Users/runner/openmm-install/lib'])
                    tools.add_rpath(join('openmm', libname), '@loader_path/../OpenMM.libs/lib')
                    print('new rpaths:', tools.get_rpaths(join('openmm', libname)))
