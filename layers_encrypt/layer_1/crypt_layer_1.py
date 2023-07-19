from symbols.symbols_layer_1 import *

#================= LEVEL 1 ============================
def Crypt_layer_1(user_input):
    hash_lvl1 = ''

    for i in user_input:

        if i in UpSymb:
            crypt_id = UpSymb.index(i) + 1
            hash_lvl1 += UpSymb[crypt_id]

        elif i in DownSymb:
            crypt_id = DownSymb.index(i)
            hash_lvl1 += Numbers_and_symbols[crypt_id]

        else:
            crypt_id = Numbers_and_symbols.index(i)
            hash_lvl1 += DownSymb[crypt_id]

    return hash_lvl1