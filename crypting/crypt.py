from layers_encrypt.layer_1.crypt_layer_1 import Crypt_layer_1
from layers_encrypt.layer_2.crypt_layer_2 import Crypt_layer_2
from layers_encrypt.salt_password.salt_password import Salt_password
from layers_encrypt.prepare.crypt_prepare import Prepare_layer
from symbols.prepare import Prepare

from layers_decrypt.layer_2 import Decrypt_layer_2

class LeCrypt:

    def Encrypt(user_input, password):
        hash_lvl1 = Crypt_layer_1(user_input)
        crypt_hash = Prepare_layer(hash_lvl1)
        crypt_hash = Crypt_layer_2(crypt_hash)
        crypt_hash = Salt_password(crypt_hash, password)

        return crypt_hash
    
    def Decrypt(hash_input, password):
        LeCrypt.Test_the_password(hash_input, password)

    def Test_the_password(hash, password):
        res = []
        iterator = -1

        #============Finding a number=============
        while(hash[iterator] != '$'):
            res.append(int(hash[iterator]))
            iterator -= 1

        res.reverse()
        strings = [str(integer) for integer in res]
        string = "".join(strings)
        integer = int(string)
        #=========================================
        #=============Finding encrypted symbols============

        iterator -= 1
        symbols = []

        while(hash[iterator] != '|'):
            symbols.append(hash[iterator])
            iterator -= 1

        symbols.reverse()
        strings = [str(integer) for integer in symbols]
        fin_symbols = "".join(strings)
        #==================================================
        s = password.strip()
        res = ''
        for c in s:
            res += Prepare[(Prepare.index(c) + integer) % len(Prepare)]

        if fin_symbols == res:

            #======Cypher processing========
            iterator = 0
            strings = []
            while(hash[iterator] != '|'):

                strings.append(hash[iterator])
                iterator += 1

            string = [str(integer) for integer in strings]
            fin_hash = "".join(string)
            #===============================

            word_from_hash = Decrypt_layer_2(fin_hash)

            print("\n[+] Text was successfully decrypted")
            print(f"\n=========================================\n\nYour text: {word_from_hash} \n\n=========================================\n")
        
        else:
            print("[-] Wrong password")