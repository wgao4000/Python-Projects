#Date: 3/07/2022
#Author: Wei Gao
#Find the eigth perfect number, a perfect number is a positive integer which is the sum of its proper divisors
# An inefficient solution

def sumOfDivisor(l):
    sum = 0
    for i in range(l):
        if(i != 0 and l % i == 0):
            sum += i
    return sum

def getPerfectNumber(n):
    i = 0
    j = 3
    listPerfectNumbers = []
    while i < n:
        if(j == sumOfDivisor(j)):
            listPerfectNumbers.append(j)
            i += 1
        j += 1 
        if(j == 1000):
            break
    print(listPerfectNumbers)
    return listPerfectNumbers[len(listPerfectNumbers) - 1]

print(getPerfectNumber(8))


# encrypt and decrypt data with Affine cipher
# E(x) = k1*x + k2 (mod 26)
# D(y) = k1^(-1) * (y - k2) (mod 26)
import re
alphaMatches = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}

numMatches = {
    "0": "a",
    "1": "b",
    "2": "c",
    "3": "d",
    "4": "e",
    "5": "f",
    "6": "g",
    "7": "h",
    "8": "i",
    "9": "j",
    "10": "k",
    "11": "l",
    "12": "m",
    "13": "n",
    "14": "o",
    "15": "p",
    "16": "q",
    "17": "r",
    "18": "s",
    "19": "t",
    "20": "u",
    "21": "v",
    "22": "w",
    "23": "x",
    "24": "y",
    "25": "z"
}

def findInverse(t):
    for i in range(26):
        if(i != 0 and (i * t) % 26 == 1):
            return i
    return 0

def encryption(plainText, k1, k2):
    res = bool(re.match('[a-zA-Z\s]+$', plainText))
    if(res):
        encryptedVal = ""
        for char in plainText.lower():
            if(char.isspace()):
                encryptedVal += char
            else:
                encryptedVal += numMatches[str((alphaMatches[char] * k1 + k2) % 26)]
        return encryptedVal
    else:
        return "The text should contain only alphabet letters or spaces"
def decryption(cipherText, k1, k2):
    res = bool(re.match('[a-zA-Z\s]+$', cipherText))
    if(res):
        decryptedVal = ""
        try:
            if(k1 % 2 == 0 or k1 % 13 == 0):
                raise Exception(str(k1) + " is not coprime with 26")
        except:
            return("Error: " + str(k1) + " and 26 must be coprime")
        else: 
            k1_inverse = findInverse(k1)
            for char in cipherText:
                if(char.isspace()):
                    decryptedVal += char
                else:
                    decryptedVal += numMatches[str(((alphaMatches[char] - k2) * k1_inverse) % 26)]
            return decryptedVal 
    else:
        return "The text should contain only alphabet letters or spaces"
print(encryption("test", 5, 7))
print(encryption("test now", 5, 7))
print(decryption("kqlfdjzvgytpaeticdhmrtwlykqlonubstx", 19, 13))
print(decryption("k q l f d j z v g y t p a e t i c d h m r t w l y k q l o n u b s t x", 19, 13))
print(decryption("kqlfdjzvgytpaeticdhmrtwlykqlonubstx", 18, 13))