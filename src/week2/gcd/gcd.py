# Uses python3
import sys, random

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_optimzed(a, b):
    if b == 0 :
        return a
    else:
        return gcd_optimzed(b , a%b)


def stress_test():
    while True:
        a = random.randint(1, 45)
        b = random.randint(1, 45)
        print("{} {}".format(a, b))
        res1 = gcd_naive(a, b)
        res2 = gcd_optimzed(a, b)
        if res1 != res2:
            print("Wrong answer: {}  {}\n".format(res1, res2))
            break
        else:
            print("OK\n")


if __name__ == "__main__":
    #stress_test()

    #input = sys.stdin.read()
    a, b = map(int, input().split())
    #print(gcd_naive(a, b))
    print(gcd_optimzed(a, b))