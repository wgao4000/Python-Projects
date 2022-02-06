#HW2 Solution
# Author: Wei Gao
# 2/06/2022
#Use find to implement a function satisfying the specification 
#def find_last(s, sub): 
      # s and sub are non-empty strings 
      # Returns the index of the last occurrence of sub in s. 
      # Returns None if sub does not occur in s 

def find_last(s, sub):
    # default condition
    if(len(sub) > len(s) or ((s.find(sub)) == -1)):
        return None
    currentIndex = s.find(sub)
    while(True):
        index = s.find(sub, currentIndex + len(sub))
        if(index == -1):
            break
        else:
            currentIndex = index
    return currentIndex
print(find_last("testnowtest", "test"))

# Given a number n, determine what the nth prime is.
import math
def isPrime(i):
    isPrime = True
    for j in range(math.floor(math.sqrt(i)) + 1):
        if(j > 1 and i % j == 0):
            isPrime = False
            break
    return isPrime 
n = int(input("Please enter a positive integer "))
def findNthPrime():
    currentPrime = 2
    if(n == 1):
        return currentPrime
    index = 1
    i = 3
    while(index < n):
        if(i % 2 != 0 and isPrime(i)):
           currentPrime = i
           index += 1
        i += 1
    return currentPrime    
print(f"The {n}th prime is {findNthPrime()}")

# Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.
n = int(input("Please enter a positive integer "))
sumOfSquares =  ((2 * n + 1) * (n + 1) * n)/6
squareOfSums = ((n * (n + 1)) /2) ** 2
print(f"The difference between the square of the sum and the sum of the squares of the first {n} natural number is {int(squareOfSums - sumOfSquares)}")

