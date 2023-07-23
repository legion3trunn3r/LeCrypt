#!/usr/bin/env python

import random
import os

from crypting.crypt import LeCrypt



	
#=============================================

user_input = input("Write your text to encrypt: ")
password = input("Write your password to encrypt: ")
password_again = input("Repeat your password: ")
if password == password_again:

	our_hash = LeCrypt.Encrypt(user_input, password)
	print(f"\n=========================================\n\nYour hash: {our_hash} \n\n=========================================")

else:
	print("[*] Please try again")

os.system("pause")
