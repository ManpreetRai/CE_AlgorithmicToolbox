# Uses python3
import random


def solution1(length_of_array, arr):
    result = 0
    for i in range(0, length_of_array):
        for j in range(i + 1, length_of_array):
            if arr[i] * arr[j] > result:
                result = arr[i] * arr[j]
    return result


def solution2(n, a):
    max1 = max2 = 0
    for i in range(0, n):
        if a[i] > max1:
            max2 = max1
            max1 = a[i]
        elif max2 < a[i] < max1:
            max2 = a[i]

    return max1 * max2


def solution3(length_of_array, arr):
    max_index1 = 0

    for i in range(0, length_of_array):
        if arr[i] > arr[max_index1]:
            max_index1 = i

    max_index2 = max_index1 - 1 if max_index1 == length_of_array - 1 else max_index1 + 1
    for j in range(0, length_of_array):
        if j != max_index1 and arr[max_index2] < arr[j]:
            max_index2 = j

    return arr[max_index1] * arr[max_index2]


def stress_test():
    while True:
        n = random.randint(1, 10) % 4 + 2
        a = []
        for i in range(0, n):
            a.append(random.randint(1, 10))

        print(n)
        print(a)
        res1 = solution1(n, a)
        res2 = solution3(n, a)
        if res1 != res2:
            print("Wrong answer: {}  {}\n".format(res1, res2))
            break
        else:
            print("OK\n")


if __name__ == "__main__":
    #stress_test()

    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)
    print(solution3(n, a))
