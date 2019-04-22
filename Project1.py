import numpy as np

#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#Creates an array of all the 5 multiplies
N5 = np.arange(5,1001,5)

#Creates an array of all the 3 multiplies
N3 = np.arange(3,1001,3)

#Sums the two arrays
N = np.sum(N5)+np.sum(N3)
print(N)

#Solution: 267333
