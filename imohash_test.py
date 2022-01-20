import os
from imohash import hashfile

slozka = "client/"

with open("hash.txt", "w") as f:
    f.write("")

def fast_scandir(dirname):
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

subfolders = [f.path for f in os.scandir(slozka) if f.is_dir()]
#subfolders.remove(slozka+"\\_MAKE_PROPERTY_XML")
for dirname in list(subfolders):
    subfolders.extend(fast_scandir(dirname))

subfolders.append("client/")
for folder in list(subfolders):
    files = [f.path for f in os.scandir(folder) if f.is_file()]
    for soubor in list(files):
        with open("hash.txt", "a") as f:
            f.write("{} : {}\n".format(soubor.replace("client/","",1),hashfile(soubor, hexdigest=True)))
