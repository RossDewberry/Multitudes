import numpy as np

#Problem 2
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
x = np.zeros()
x1 = 1
x2 = 2
print(x1)
print(x2)

x = x1 + x2

s = []
s=2
while x<=(4 * 10**6):
    print(x)
    x = x+s
    s = x-s
//TODO: Sum even terms
