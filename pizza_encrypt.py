import random
import string
import os
import sys
from functools import wraps


SYMBOLS = string.ascii_uppercase + string.ascii_lowercase + string.digits

def pizza_encrypt(string):
    after_encrypt = string
    after_ecrypt_string = ''
    for el in range(1,len(string)):
        after_encrypt[el],after_encrypt[el - 1] = after_encrypt[el - 1],after_encrypt[el]

    for el in after_encrypt:
        after_ecrypt_string += el + random.choice(SYMBOLS)
    return after_ecrypt_string

def pizza_decrypt(string):
    after_encrypt = string[::2]
    after_ecrypt_string = ''
    for el in reversed(range(1,len(after_encrypt))):
        after_encrypt[el - 1],after_encrypt[el] = after_encrypt[el],after_encrypt[el - 1]
    for el in after_encrypt:
        after_ecrypt_string += el
    return after_ecrypt_string
