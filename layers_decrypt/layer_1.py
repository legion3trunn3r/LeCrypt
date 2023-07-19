from symbols.symbols_layer_1 import *

#================LEVEL 1======================
def Decrypt_layer_1(text_prepare):

    text_lvl1= ''
    for i in text_prepare:
        if i in UpSymb:
            hash_id = UpSymb.index(i) - 1
            text_lvl1 += UpSymb[hash_id]
        elif i in DownSymb:
            hash_id = DownSymb.index(i)
            text_lvl1 += Numbers_and_symbols[hash_id]
        else:
            hash_id = Numbers_and_symbols.index(i)
            text_lvl1 += DownSymb[hash_id]
            
    return text_lvl1