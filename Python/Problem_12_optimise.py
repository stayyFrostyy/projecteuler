import math
def get_factors(n):
    return sum(2 for i in range(1, round(math.sqrt(n) + 1)) if not n % i)

def gen_triangles(lim):
    l = 1
    while l <= lim:
        yield sum(range(l + 1))
        l += 1

def test_triangles():
    triangles = gen_triangles(100000)
    for i in triangles:
        if get_factors(i) > 499:
            return i

print(test_triangles())