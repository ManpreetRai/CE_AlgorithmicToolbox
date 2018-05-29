# Uses python3
import random


def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_optimized(n):
    arr_ele = []
    for i in range(0, n + 1):
        if i <= 1:
            arr_ele.append(i)
        else:
            arr_ele.append(arr_ele[i - 2] + arr_ele[i - 1])

    if len(arr_ele) > 1:
        return arr_ele[n - 2] + arr_ele[n - 1]
    else:
        return n


def stress_test():
    while True:
        n = random.randint(0, 45)
        print(n)
        res1 = calc_fib(n)
        res2 = calc_fib_optimized(n)
        if res1 != res2:
            print("Wrong answer: {}  {}\n".format(res1, res2))
            break
        else:
            print("OK\n")

if __name__ == '__main__':
    #stress_test()

    n = int(input())
    print(calc_fib_optimized(n))
