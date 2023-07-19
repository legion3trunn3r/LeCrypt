from symbols.symbols_layer_2 import *
from symbols.prepare import Prepare

from layers_decrypt.layer_1 import Decrypt_layer_1

#=========TRANSFERING FROM LEVEL2 TO LEVEL1 FOR ENCRYPT=================
def Transfering_from_lvl2_to_lvl1(text_lvl2):
    text_prepare = ''

    for i in text_lvl2:

        if i == ":":
            text_prepare += ":"

        else:
            text_prepare += str(special_numbers_nr1.index(i))

    lists = text_prepare.split(":")			
    text_prepare = ''

    for i in lists:
        text_prepare += Prepare[int(i)]

    return Decrypt_layer_1(text_prepare)

#========LEVEL 2============================
def Decrypt_layer_2(hash_input):
        text_lvl2 = ''
        count = 0
                
        for i in hash_input:
                        
            if i == "<" or i == ">":         
                if count + 1 != len(hash_input):
                    text_lvl2 += ":"
            else:
                hash_id = special_numbers_nr2.index(i)
                text_lvl2 += special_numbers_nr1[int(hash_id)]
                                
            count += 1

        return Transfering_from_lvl2_to_lvl1(text_lvl2)

	#============================================