import random

from symbols.prepare import Prepare

#================Salt(password to decrypt)============
def Salt_password(hash_lvl2, password):
    n = random.randrange(1, 100)
    s = password.strip()
    res = ''
    
    for c in s:
        res += Prepare[(Prepare.index(c) + n) % len(Prepare)]

    # to decrypt cezar: example: 5 -> decrypt -> -5
    hash_lvl2 = hash_lvl2 + "|" + res
    hash_lvl2 = hash_lvl2 + "$" + str(n)
    print("[+] Hash was successfully created")
    return hash_lvl2