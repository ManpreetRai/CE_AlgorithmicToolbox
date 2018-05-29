# Uses python3

import sys
def binary_search(a, low, high, key):

    # write your code here
    if high < low:
        return - 1
    mid = low + (high - low) // 2

    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search(a, low, mid - 1, key)
    else:
        return binary_search(a, mid + 1, high, key)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    # for x in data[n + 2:]:
    #     print(linear_search(a, x), end=' ')
    # print()
    for x in data[n + 2:]:
        print(binary_search(a, 0, len(a) -1, x), end=' ')
