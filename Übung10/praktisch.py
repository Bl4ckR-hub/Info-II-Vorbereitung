# Aufgabe 1

import sys

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar(key, mes):
    res = ''
    for i in mes:
        res += alphabet[(alphabet.index(key) + alphabet.index(i) + 1) % 26]
    return res

def check_mes(mes):
    if (not mes):
        return True
    return mes[0] in alphabet and check_mes(mes[1:])

def line_schieberegister():
    if (len(sys.argv) < 3 or len(sys.argv[1]) != 8):
        exit()
    if (not check_mes(sys.argv[1])):
        exit()
    
    mes = sys.argv[1]
    m = ''
    n = int(sys.argv[2])
    while (n > 0):
        m += mes[0]
        b = caesar(caesar(mes[1], mes[3]), caesar(mes[6], mes[7]))
        tmp = mes[1:]
        tmp += b
        mes = tmp
        n -= 1
    return m

def char_counter(mes):
    e = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for ch in mes:
        e[alphabet.index(ch)] += 1
    return e

# Aufgabe 2
def tranpose_decrypt(string, length):
    if (length <= 0):
        exit()
    d = []
    indi = -1
    for i in range(len(string)):
        if (i % length == 0):
            indi += 1
            d.append(string[i])
        else:
            d[indi] += string[i]
    while(len(d[indi]) < length):
        d[indi] += 'X'

    decrypted = ''
    for i in range(length):
        for w in d:
            decrypted += w[i]
    return decrypted


def transpose_encrypt(dec, length):
    en = []
    for index in range(len(dec)):
        if (index < (len(dec) // length)):
            en.append(dec[index])
        else:
            en[index % (len(dec) // length)] += dec[index]

    encrypt = ''
    for strs in en:
        encrypt += strs
    return encrypt


def transpose(mes, length, decode):
    if (decode):
        return tranpose_decrypt(mes, length)
    else:
        return transpose_encrypt(mes, length)
    



