
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    ans = 0
    for i in range(9999, 100, -1):
        for j in range(i, 100, -1):
            temp = i * j
            if temp > ans:
                strTemp = str(temp)
                if strTemp == strTemp[::-1]:
                    ans = temp

    return ans


print(main())


