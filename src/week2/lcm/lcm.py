# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def gcd_optimzed(a, b):
    if b == 0:
        return a
    else:
        return gcd_optimzed(b, a % b)


def lcm_optimized(a, b):
    gcd = gcd_optimzed(a, b)
    lcm = (a * b) // gcd
    return lcm


if __name__ == '__main__':
    a, b = map(int, input().split())
    #print(lcm_naive(a, b))
    print(lcm_optimized(a, b))
