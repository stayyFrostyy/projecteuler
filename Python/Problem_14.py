
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# note: Once the chain starts the terms are allowed to go above one million.

def nextN(n):
    if n % 2 == 0:
        return n/2
    else:
        return (n*3) + 1

def main():
    limit = 999999
    n = 0
    chain_len = 0
    temp_chain_len = 0
    chain_num = 0

    for i in range(1, limit):
        temp_chain_len = 0
        n = i
        while n != 1:
            n = nextN(n)
            temp_chain_len += 1

            if n == 1:
                break

        if n == 1:
                # print("i is 1")
                # print(temp_chain_len, " || ", chain_len)
                # print(chain_num)
                if temp_chain_len > chain_len:
                    # print(temp_chain_len, " || ", chain_len)
                    # print(i)
                    chain_len = temp_chain_len
                    chain_num = i

    return chain_num
        
print(main())


    
