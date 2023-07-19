#!/usr/bin/env python

import os

from crypting.crypt import LeCrypt

hash_input = input("Write your hash to decrypt: ")
password = input("Write your password: ")

try:
	LeCrypt.Decrypt(hash_input, password)

except ValueError:
	print("\n\n[*] This symbol can't be decrypted")

os.system("pause")