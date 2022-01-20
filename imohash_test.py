import os
from imohash import hashfile

with open("hash.txt", "w") as f:
    f.write("")

for pack in os.listdir("pack/"):
    pack_lokace = "pack/{}".format(pack)
    with open("hash.txt", "a") as f:
        f.write("{} : {}\n".format(pack_lokace,hashfile(pack_lokace, hexdigest=True)))
