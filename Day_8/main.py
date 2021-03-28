# Day 8
# Functions with inputs

# Goal Caesar Cipher

import random
from source_files import alphabet as alpha

# Todo 1: Get the user's input
direction = input(f"Type 'encode' to encrypt, type 'decode' to decrypt: \n")
secret_text = input("Type you secret message: \n").lower()
shift_counter = int(input("Type the shift number: \n"))

# Todo 2: Create the encryption logic

'''Create function takes 3 input.'''


def ceasar(start_text, crypto_counter, crypto_Ops):
    end_text = ""
    if crypto_Ops == "decode":
        crypto_counter *= -1
    for char in start_text:
        for char in start_text:
            position = alpha.index(char)
            new_position = position + crypto_counter
            end_text += alpha[new_position]
    print(f"The {crypto_Ops}d text is: \n{end_text}")


ceasar(start_text=secret_text, crypto_counter=shift_counter, crypto_Ops=direction)
