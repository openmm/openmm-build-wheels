import os
import zipfile

zips = os.listdir('.')
os.makedirs('wheels')
for z in zips:
    if zipfile.is_zipfile(z):
        zip = zipfile.ZipFile(z)
        for name in zip.namelist():
            if not os.path.exists(os.path.join('wheels', name)):
                zip.extract(name, path='wheels')
