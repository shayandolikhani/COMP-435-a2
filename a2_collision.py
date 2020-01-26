import hashlib
import random
import string


def find_collision(n):
    dict = {}
    test = False
    while not test:
        m = hashlib.sha256()
        new_string = ''.join(random.choice(string.printable) for i in range(random.randint(1, 32)))
        m.update(new_string.encode("ascii"))
        result = m.digest()
        if result[:n] not in dict:
            dict[result[:n]] = new_string;
        elif new_string != dict[result[:n]]:
            return new_string, dict[result[:n]]
