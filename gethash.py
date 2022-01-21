import os
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

slozka = "client/"
filelist = "filelist.xml"

with open(filelist, "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write("<PatchList>\n")
    f.write("\t<PatchFiles>\n")

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
        with open(filelist, "a") as f:
            f.write("\t\t<PatchFile>\n")
            f.write("\t\t\t<Name>{}</Name>\n".format(soubor.replace("client/","",1).replace("/","\\")))
            f.write("\t\t\t<Hash>{}</Hash>\n".format(md5(soubor)))
            f.write("\t\t</PatchFile>\n")

with open(filelist, "a") as f:
    f.write("\t</PatchFiles>\n")
    f.write("</PatchList>")
