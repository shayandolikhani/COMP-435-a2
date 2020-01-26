import hashlib
import random
import string


def find_preimage(target, n):
    test = False
    while not test:
        m = hashlib.sha256()
        new_string = ''.join(random.choice(string.printable) for i in range(random.randint(1, 32)))
        m.update(new_string.encode("ascii"))
        result = m.digest()
        if result[:n] == target[:n]:
            return new_string
