# Uses python3
import sys, random

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_optimized(n):
    arr_ele = []
    for i in range(0, n + 1):
        if i <= 1:
            arr_ele.append(i)
        else:
            rem = (arr_ele[i - 2] + arr_ele[i - 1]) % 10
            arr_ele.append(rem)

    if len(arr_ele) > 1:
        return (arr_ele[n - 2] + arr_ele[n - 1]) % 10
    else:
        return n


def stress_test():
    while True:
        n = random.randint(0, 1000)
        print(n)
        res1 = get_fibonacci_last_digit_naive(n)
        res2 = get_fibonacci_last_digit_optimized(n)
        if res1 != res2:
            print("Wrong answer: {}  {}\n".format(res1, res2))
            break
        else:
            print("OK\n")


if __name__ == '__main__':
    #input = sys.stdin.read()
    #stress_test()

    n = int(input())
    #print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_optimized(n))
