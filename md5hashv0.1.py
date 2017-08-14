import hashlib

hasher = hashlib.md5()
with open('403441.gif', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print(hasher.hexdigest())
