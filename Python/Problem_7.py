
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from tkinter import N


def isPrime(n):
    pDivis = range(2, int(n**.5) + 1)
    for i in pDivis:
        if n % i == 0:
            return False
        
    return True


def main(n2):
    numPrimes = 1
    n = 2
    while numPrimes < n2:
        n = n + 1
        if isPrime(n) == True:
            numPrimes = numPrimes + 1
    
    return n


print(main(10001))