
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def isPrime(n):
    pDivis = range(2, int(n**.5) + 1)
    for i in pDivis:
        if n % i == 0:
            return False
        
    return True

def main(n2):
    prime = 2
    n = 1
    ans = 0

    while prime <= n2:
        n = n + 1
        if isPrime(n) == True:
            prime = n

            if prime >= n2:
                break
            
            ans = ans + n

    return ans


print(main(2000000))
