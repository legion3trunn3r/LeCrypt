import random

from symbols.symbols_layer_2 import *
from symbols.prepare import Prepare

#=========TRANSFERING FROM LEVEL 1 TO PREPARE BEFORE LEVEL 2 =================
def Prepare_layer(hash_lvl1):
    count = 0
    hash_prepare = ''

    while count < len(hash_lvl1):
        hash_lvl_prepare = str(Prepare.index(hash_lvl1[count]))

        for transfer in hash_lvl_prepare:
            hash_prepare += special_numbers_nr1[int(transfer)]

        hash_prepare += ":"
        count += 1
    
    iterator = 0
    list_of_hash = list(hash_prepare)
	
    for i in hash_prepare:
        if i == ":":
            list_of_hash[iterator] = random.choice(two_simbols_for_dualpoint)
            hash_prepare = ''.join(list_of_hash)
		
        iterator += 1

    return hash_prepare