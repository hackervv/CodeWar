# --coding: utf-8 -- 
import operator
from functools import reduce
def persistence(n):
    """ Write a function,persistence,that takes in a positive parameter num and return its multiplicative persistence,which is the number of times you must multiply the digits in num until you reach a single digit """
    i = 0
    while n>= 10:
        # reduce(): 会对参数序列中元素进行累积
        # operate：
        n = reduce(operator.mul,[int(x) for x in str(n)],1)
        i += 1
    return i

print(persistence(999))