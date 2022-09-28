
# The sum of the squares of the first ten natural numbers is, 1^^2 + 2^^2 ... 10^^2 = 385

# The square of the sum of the first ten natural numbers is, (1+2+3...+10)^^2 == 55^^2 == 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def main():
    total1 = 0
    total2 = 0
    for i in range(101):
        total1 = total1 + i**2
        total2 = total2 + i

    return (total2**2) - total1


print(main())