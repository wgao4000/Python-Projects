# Date: 2/21/2022
# Author: Wei Gao
# Find the smallest five consecutive composite integers.
import math
def isPrime(i):
    isPrime = True
    for j in range(math.floor(math.sqrt(i)) + 1):
        if(j > 1 and i % j == 0):
            isPrime = False
            break
    return isPrime

def findConseCompo(n):
    i  = 4
    l1 = []
    while len(l1) < n:
        if(not(isPrime(i)) and (len(l1) == 0 or (i - 1 in l1))):
            l1.append(i)
        else: 
            l1.clear()
        i += 1
    print(l1)

findConseCompo(5)
findConseCompo(6)
findConseCompo(7)
findConseCompo(10)