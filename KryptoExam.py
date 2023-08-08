alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_down = "abcdefghijklmnopqrstuvwxyz"

def encode(string):
    encoded = ""
    for char in string:
        if (char.upper() in alphabet_upper):
            encoded += char.upper()
    return encoded;



# Blockschiffre mit Beispiel Caesar mit Schlüssel C

def char_to_index(char):
    if (char in alphabet_upper):
        return alphabet_upper.index(char)+100
    elif (char in alphabet_down):
        return alphabet_down.index(char)
    else: return -1

def index_to_char(index):
    if index > 99:
        return alphabet_upper[index-100]
    else:
        return alphabet_down[index]
    
def caesar(key, message):
    encoded = ""
    for char in message:
        if (char_to_index(char) > 99):
            encoded += index_to_char(((char_to_index(char)-100 + key) % 26) + 100)
        elif char_to_index(char) > 0:
            encoded += index_to_char((char_to_index(char) + key) % 26)
        else:
            raise ValueError('Characater ' + char + ' is not in the alphabet')
    return encoded


# Encoding Fntction
def encode_caesar(key, message):
    decoded = ""
    for char in message:
        if (char_to_index(char) > 99):
            decoded += index_to_char(((char_to_index(char)-100 - key) % 26) + 100)
        elif char_to_index(char) > 0:
            decoded += index_to_char((char_to_index(char) - key) % 26)
        else:
            raise ValueError('Characater ' + char + ' is not in the alphabet')
    return decoded

print(caesar(3, 'helloworld'))
print(caesar(3, 'HELLOWORLD'))

print(encode_caesar(3, caesar(3, 'helloworld')))
print(encode_caesar(3, caesar(3, 'HELLOWORLD')))