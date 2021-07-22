# -*- coding: utf-8 -*-
"""Hacking Caeser cipher
"""

# Code to use Brute force on Caesar cipher if you don't have the key.
msg=input("Enter encrypted message: ")
msg=msg.upper()
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)):

    # Set translated to the blank string so that the previous iteration's value for translated is cleared.
    translated = ''

    # run the encryption/decryption code on each symbol in the message
    for i in msg:
        if i in LETTERS:
            num = LETTERS.find(i) # get the number of the symbol
            num = num - key  #to get the orignal letter (before the shifting)

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # add number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add the letter(i) without encrypting/decrypting. (For spaces or chars other than alphabets)
            translated = translated + i

    # display the current key being tested, along with its decryption
    print('Key %s: %s' % (key, translated))







