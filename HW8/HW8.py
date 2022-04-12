#Author: Wei Gao
#Date: 04/05/2022
# An implementation of the ElGamal Encryption
import secrets
import sympy 
# P = 2946901
P = sympy.randprime(1000000000000000000000, 1000000000000000000000000)
print("the prime is " + str(P))
#M = "396"
M = "Hello world"
alphaMatches = {
    "a": '00',
    "b": '01',
    "c": '02',
    "d": '03',
    "e": '04',
    "f": '05',
    "g": '06',
    "h": '07',
    "i": '08',
    "j": '09',
    "k": '10',
    "l": '11',
    "m": '12',
    "n": '13',
    "o": '14',
    "p": '15',
    "q": '16',
    "r": '17',
    "s": '18',
    "t": '19',
    "u": '20',
    "v": '21',
    "w": '22',
    "x": '23',
    "y": '24',
    "z": '25',
    " ": '26'
}

numMatches = {
    "00": "a",
    "01": "b",
    "02": "c",
    "03": "d",
    "04": "e",
    "05": "f",
    "06": "g",
    "07": "h",
    "08": "i",
    "09": "j",
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
    "25": "z",
    "26": " "
}
secretsGenerator = secrets.SystemRandom()
def getKeys(P):
    g = 7                               
    privateKey = secretsGenerator.randint(2, 13)
    publicKey = int((g ** privateKey) % P)  # big X
    return {publicKey: privateKey}   

def textToInt(text_val):
    emptyText = ''
    for t in text_val.lower():
      emptyText += alphaMatches[t]
    return int(emptyText)

def intToText(int_val):
    if(not(len(str(int_val)) % 2 == 0)):
      int_val = '0' + str(int_val) 
    emptyInt = ''
    for i in range(0, len(int_val), 2):
      tmp = str(int_val[i]) + str(int_val[i + 1])
      emptyInt +=  numMatches[tmp]
    return emptyInt
# key generation:
aliceKeys = getKeys(P)
# print("aliceKeys " + str(list(aliceKeys.keys())[0]), str(list(aliceKeys.values())[0]))

# encryption:
bobKeys = getKeys(P)
# print("bobKeys " + str(list(bobKeys.keys())[0]), str(list(bobKeys.values())[0]))
alicePublicKey = int(list(aliceKeys.keys())[0]) # alice public key
bobPrivateKey = int(list(bobKeys.values())[0])# bobs private key

cipherMessage = int((int(textToInt(M)) * (alicePublicKey ** bobPrivateKey) % P) % P)
bobPublicKey = int(list(bobKeys.keys())[0]) # bobs public Key
print("The original message is " + str(textToInt(M)))


#decryption:
alicePrivateKey = int(list(aliceKeys.values())[0]) # alice private key
commonKey = int((bobPublicKey ** alicePrivateKey) % P)
# Python 3.8 only inverseCommonKey = pow(commonKey, -1, P)
inverseCommonKey = int(sympy.mod_inverse(commonKey, P))
retrievedMessage = int((inverseCommonKey * cipherMessage) % P)
print("The decrypted message is " + intToText(int(retrievedMessage)))
