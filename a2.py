import sys
import hashlib

m = hashlib.sha1()
m.update(b"Test string!")
m.hexdigest()

m = hashlib.sha256()
m.update(b"second test string!")
m.hexdigest()

m = hashlib.md5()
m.update(b"third test string!")
m.hexdigest()

filename = input("Input file name: ")
with open(filename, "rb") as f:
    text = f.read()
H1 = hashlib.sha256(text)
H1.hexdigest()

filename = input("Input file name: ")
with open(filename, "rb") as f:
    text = f.read()
H2 = hashlib.sha256(text)
H2.hexdigest()
