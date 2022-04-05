import secrets
from math import pow
import sympy 

P = 2946901
M = "396"
secretsGenerator = secrets.SystemRandom()
def getKeys(P):
    g = 7                               
    privateKey = secretsGenerator.randint(2, 13)
    publicKey = int((g ** privateKey) % P)  # big X
    return {publicKey: privateKey}    

# key generation:
aliceKeys = getKeys(P)
# print("aliceKeys " + str(list(aliceKeys.keys())[0]), str(list(aliceKeys.values())[0]))

# encryption:
bobKeys = getKeys(P)
# print("bobKeys " + str(list(bobKeys.keys())[0]), str(list(bobKeys.values())[0]))
alicePublicKey = int(list(aliceKeys.keys())[0]) # alice public key
bobPrivateKey = int(list(bobKeys.values())[0])# bobs private key

t1 = (int(M) * (alicePublicKey ** bobPrivateKey) % P) % P
cipherMessage = int((int(M) * (alicePublicKey ** bobPrivateKey) % P) % P)
bobPublicKey = int(list(bobKeys.keys())[0]) # bobs public Key
print("The original message is " + M)


#decryption:
alicePrivateKey = int(list(aliceKeys.values())[0]) # alice private key
commonKey = int((bobPublicKey ** alicePrivateKey) % P)
# Python 3.8 only inverseCommonKey = pow(commonKey, -1, P)
inverseCommonKey = int(sympy.mod_inverse(commonKey, P))
retrievedMessage = int((inverseCommonKey * cipherMessage) % P)
print("The decrypted message is " + str(retrievedMessage))
