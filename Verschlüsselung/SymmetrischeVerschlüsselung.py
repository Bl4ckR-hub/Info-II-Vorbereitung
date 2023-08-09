alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_length = len(alphabet)

# diese Funktion entfernt aus der Nachricht alle nicht dem Alphabet gehörigen Zeichen
def encode(text):
    encoded = ""
    for c in text:
        if (c.upper() in alphabet):
            encoded += c.upper()
    return encoded

# Nun kommen wir zur Caesar-Verschlüsselung
# Caesar-Verschlüsselung zählt zu Symmetrischen Verschlüsselungsalgorithmen und ist den BlockSchiffren zuzuordnen
def caesar_encrypt(key, message):
    if (key not in alphabet):
        raise ValueError('Key not in alphabet')
    encrypted = ""
    for c in message:
        if c not in alphabet:
            raise ValueError('The Character ' + c + ' is not in the alphabet')
        encrypted += alphabet[(alphabet.index(c) + alphabet.index(key)) % alphabet_length]
    return encrypted

def caesar_decrypt(key, message):
    decrypted = ""
    for c in message:
        if c not in alphabet:
            raise ValueError('The Character ' + c + ' is not in the alphabet')
        decrypted += alphabet[(alphabet.index(c) - alphabet.index(key)) % alphabet_length]
    return decrypted

# Nach der Caesar-Verschlüsselung wenden wir uns dem One-Time-Pad.
# Dieses zählt ebenso zu symmetrischen Verschlüsselungsalgorithmen und ist dem Stromschiffren zuzuordnen, weil wir für jeden źu verschlüsselenden Block einen eigenen Key benötigen
def one_time_pad_encrypt(key, message):
    if (len(key) != len(message)):
        raise IndexError('Your Key is not long enough or too long')
    encrypted = ""
    for k, c in zip(key, message):
        if (k not in alphabet):
            raise ValueError('Key not in alphabet')
        encrypted += caesar_encrypt(alphabet[(alphabet.index(k)+1) % alphabet_length], "" + c)
    return encrypted

def one_time_pad_decrypt(key, message):
    if (len(key) != len(message)):
        raise IndexError('Your Key is not long enough or too long')
    encrypted = ""
    for k, c in zip(key, message):
        if (k not in alphabet):
            raise ValueError('Key not in alphabet')
        encrypted += caesar_decrypt(alphabet[(alphabet.index(k)+1) % alphabet_length], c)
    return encrypted

# Nun brauchen wir einen zufälligen Schlüsselgenerator
# Dafür nutzen wir LInearen Schiebregister mit der Rückkopplungsfunktion der Verschlüssleungsfunktio  der Caesar-Verschlüsselung

def keygen(start_key, counter):
    start_key = start_key[::-1]
    key = ""
    for _ in range(counter):
        key += start_key[len(start_key)-1]
        tmp = ""
        res = one_time_pad_encrypt(one_time_pad_encrypt(start_key[len(start_key)-1], start_key[len(start_key)-3]), one_time_pad_encrypt(start_key[1], start_key[0]))
        tmp += res
        for i in range(0, len(start_key)-1):
            tmp += start_key[i]
        start_key = tmp
    return key


print('Give me the message, you want to send: ')
message = input()
message = encode(message)


print('This is your key: ')
start = message[::-1]
start = start[0::len(start)//4]
print(keygen(start, len(message)))

print('This is the encrypted message: ')
print(one_time_pad_encrypt(keygen(start, len(message)), message))