from os.path import join
import os
import sys

# Figure out what platform suffix the wheels should have.

wheeldir = sys.argv[1]
for filename in os.listdir(wheeldir):
    if filename.endswith('.whl') and not filename.endswith('-any.whl'):
        suffix = filename[filename.rfind('-'):]
        break

# Rename any that are currently marked as platform independent.

for filename in os.listdir(wheeldir):
    if filename.endswith('-any.whl'):
        newname = filename[:-8]+suffix
        os.rename(join(wheeldir, filename), join(wheeldir, newname))
