# Date: 2-28-2022
# Author: Wei Gao

# implement the Caesar cipher (ROT13) with two functions
# the encryption function takes a plaintext, and transform it into a ciphertext
# the decryption function takes a ciphertext, and transform it into a plaintext
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

def encryption(plainText):
    res = bool(re.match('[a-zA-Z\s]+$', plainText))
    if(res):
        cipherText = ""
        for char in plainText.lower():
            if char.isspace():
                cipherText += char
            else:  
                shiftedValue = int(alphaMatches[char]) + 13
                if(shiftedValue > 25):
                    shiftedValue %= 26
                cipherText += numMatches[str(shiftedValue)] 
        return cipherText 
    else: 
        return "The text should contain only alphabet letters or spaces"

def decryption(cipherText):
    res = bool(re.match("[a-zA-Z\s]+$", cipherText))
    if(res):
        plainText = ""
        for char in cipherText.lower():
            if char.isspace():
                plainText += char
            else:
                shiftedValue = int(alphaMatches[char]) - 13
                if(shiftedValue < 0):
                    shiftedValue %= 26
                plainText += numMatches[str(shiftedValue)] 
        return plainText 
    else: 
        return "The text should contain only alphabet letters or spaces"

print(encryption("abcdefghijklmnopqrstuvwxyz"))
print(decryption("nopqrstuvwxyzabcdefghijklm"))
print(encryption("t!tttt"))
print(decryption("123ttt"))
print(encryption("Test now Test now"))
print(encryption("test now Test now"))
print(decryption("Grfg abj grfg abj"))