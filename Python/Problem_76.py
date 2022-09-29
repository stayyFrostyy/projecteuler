
# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum of at least two positive integers?

def main(n):
    n_sums = [0] * (n + 1)
    n_sums[0] = 1

    for i in range(1, n):
        for j in range(i, n + 1):
            n_sums[j] = n_sums[j] + n_sums[j - i]

    return n_sums[n]

print(main(100))