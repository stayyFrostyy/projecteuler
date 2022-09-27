
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def main(number):
    i = 2
    while number > 1:
        while number % i == 0:
            number /= i
        i = i + 1

    return i - 1


print(main(600851475143))