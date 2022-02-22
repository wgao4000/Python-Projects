# Date: 2/15/2022
# Author: Wei Gao
"""
implement a function satisfying the following specification. 
def f(L1, L2): 
      # L1, L2 lists of same length of numbers 
      # returns the sum of raising each element in L1 
      # to the power of the element at the same index in L2 
      # For example, f([1,2], [2,3]) returns 9
"""
def myfunc(L1, L2, L3):
    sum = 0
    for i in map(lambda x, y: x** y, L1, L2):
        sum += i
    return sum
print(myfunc([1,2], [2,3],[4,5]))