import os,sys
import hashlib


def hashfile(path):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read()   
    hasher.update(buf)

    afile.close()
    return hasher.hexdigest()

def findDup(dir, dups, abs_path_set):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)


		path=os.path.realpath(path)
		if path in abs_path_set:
			continue
		else:
			abs_path_set[path]=1


		if os.path.isfile(path):
			file_hash = hashfile(path)
			if file_hash in dups:
				dups[file_hash].append(path)
			else:
				dups[file_hash]=[path]

		else:
			findDup(path, dups, abs_path_set)

	return dups

dups={}
abs_path_set={}
findDup("test", dups, abs_path_set)
print dups
print abs_path_set