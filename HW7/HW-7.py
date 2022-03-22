# Author Wei Gao
# Date: 3/22/2022
import random
import sympy
"""
Create an implementation of the Diffie-Hellman key exchange protocol with Python.
Diffie-Hellman key exchange
Alice and Bob use Diffie-Hellman key exchange to share secrets. They start with prime
numbers, pick private keys, generate and share public keys, and then generate a shared
secret key.
"""
P = 2946901
G = 7

def diffieHellmanProtocol(p, g):
    try:
        if(not(sympy.isprime(p))):
           raise Exception(p + " is not a prime.") 
    except: 
        print("The first value you used is not a prime")
    else:
        randVal = random.randrange(2, p)
        userPublicKey = pow(g, randVal) % p
        # print("randVal is", randVal)
        # print("userPublicKey is",  userPublicKey)
        return {randVal: userPublicKey}

aliceKeys = diffieHellmanProtocol(P, G)
bobKeys = diffieHellmanProtocol(P, G)
commonKey = pow(list(aliceKeys.values())[0], list(bobKeys.keys())[0]) % P  
commonKey2 = pow(list(bobKeys.values())[0], list(aliceKeys.keys())[0]) % P

print(commonKey, commonKey2)






    
    
