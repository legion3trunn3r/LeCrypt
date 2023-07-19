from symbols.symbols_layer_2 import *

#==================== LEVEL 2 ============================
def Crypt_layer_2(hash_prepare):
	hash_lvl2 = ''
	
	for i in hash_prepare:
		
		if i == "<" or i == ">":
			hash_lvl2 += i
			
		else:
			hash_id = special_numbers_nr1.index(i)
			hash_lvl2 += special_numbers_nr2[int(hash_id)]
		
	return hash_lvl2