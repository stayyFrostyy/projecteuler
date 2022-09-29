
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def main():
    ans = 1000
    c = 1
    found = False

    for a in range(1, 1001):
        
        for b in range(a+1, a+1001):
            
            c = ans - a - b

            if a**2 + b**2 == c**2:
                found = True
                break
    
        if found == True:
            print(a, "*", b, "*", c)
            return a*b*c
            break

print(main())
