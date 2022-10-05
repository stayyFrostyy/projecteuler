
# 2^^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^^1000?

def main():
    number = str(2**1000)
    numints = []
    for i in number:
        numints.append(int(i))
    
    total = 0
    for i in range(len(numints)):
        total += numints[i]

    return total

print(main())