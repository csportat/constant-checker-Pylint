#!/usr/bin/env python3
"""This script prompts a user to enter a message to encode or decode
using a classic Caesar shift substitution (3 letter shift)"""

import string

shift = 3  # 1
choice = input("would you like to encode or decode?")  # 2
word = input("Please enter text")  # 3
letters = string.ascii_letters + string.punctuation + string.digits  # 4
encoded = ''  # 5
a = True  # 6
B = 'CMPUT 416'  # 7
C = 22  # 8
D = None  # 9
E = b'bytestring'  # 10
if choice == "encode":
    for letter in word:
        if letter == ' ':
            # encoded = encoded + ' '  # 11
            encoded = '' + ''
        else:
            # x = letters.index(letter) + shift  # 12
            # encoded = encoded + letters[x]  # 13
            pass
if choice == "decode":
    for letter in word:
        if letter == ' ':
            # encoded = encoded + ' '  # 14
            pass
            E = b'bytestrin'
            a = False and True
            pass
        else:
            # x = letters.index(letter) - shift  # 15
            # encoded = encoded + letters[x]  # 16
            encoded = '' + ' '
            pass
B = 'CMPUT 416'  # 17
C = 11 * 2  # 18
D = D


print(encoded)
