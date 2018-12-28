import hashlib
from Tkinter import Tk
from tkinter.filedialog import askopenfilename


def FileSelection():
    global filename
    global BLOCKSIZE
    BLOCKSIZE = 65536
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    HSHA512()
    HSHA384()
    HSHA256()
    HSHA224()
    HSHA1()
    HMD5()

def HSHA512():
    hasher=hashlib.sha512()
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    print "\nSHA512",hasher.hexdigest()

def HSHA384():
    hasher=hashlib.sha384()
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    print "\nSHA384",hasher.hexdigest()

def HSHA256():
    hasher=hashlib.sha256()
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    print "\nSHA256",hasher.hexdigest()

def HSHA224():
    hasher=hashlib.sha224()
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    print "\nSHA224",hasher.hexdigest()

def HSHA1():
    hasher=hashlib.sha1()
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    print"\nSHA1",hasher.hexdigest()

def HMD5():
    hasher=hashlib.md5()
    with open(filename, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    print "\nMD5",hasher.hexdigest()

FileSelection()
