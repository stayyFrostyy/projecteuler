
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?


# Binomial Coefficient of n k
# Calculates Pascal's triangle
# Formula >> n! / k! * (n-k)!

# Lattice Paths
# (0,0) to (20,20)
# Number of paths from point to point is calculated by c(a + b, a)
# Binomial Coefficient >> C(a + b, a)

from math import factorial

def calc_bco(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# grid size 20x20
print(calc_bco(20+20, 20))