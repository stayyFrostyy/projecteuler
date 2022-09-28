
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Answer must also be divisible by 1-10 
# therefore I can start at 2520 and increment by 2520
# and only check numbers 11-20

def main():
    num = 2520
    found = False
    while found != True:
        num = num + 2520
        divis = True
        for i in range(11,20):
            if (num % i != 0):
                divis = False
                break
        
        if divis == True:
            found = True

    return num

print(main())

            

