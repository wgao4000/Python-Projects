# author: Weizheng Gao
# Write a program that asks the user to input 10 integers and prints the largest odd number that was entered.
largestVal = int(input("Please enter an integer "))
for i in range(9):
    currentVal = int(input("Please enter an integer "))
    if(largestVal < currentVal and currentVal % 2 == 1):
        largestVal = currentVal
if(largestVal % 2):
    print("The largest odd number entered is " + str(largestVal))
else:
    print("You did not enter an odd number")

# Write a problem that prints the sum of the prime numbers greater than 2 and less than 1000
import math
sum = 0
for i in range(1000):
    if(i > 2 and i % 2 == 1):
        isPrime = False
        # primary test only goes up to the floor function of the square root of i
        for j in range(math.floor(math.sqrt(i)) + 1):
    #   for j in range(i):
            if(j > 1 and i % j == 0):
                isPrime = True
                break
        if(not(isPrime)):
            sum += i
   
print("The sum of the prime numbers greater than 2 and less than 1000 is " + str(sum))
