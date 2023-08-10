alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_unlocker(message):
    str = ""
    for i in range(26):
        print(caesar_decrypt(message, i))

def caesar_decrypt(message, key):
    str = ""
    for c in message:
        str += alphabet[(alphabet.index(c) - key) % 26]
    return str