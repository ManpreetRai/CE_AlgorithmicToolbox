# Uses python3
import sys


def get_majority_element(a, left, right):
    sorted_a = sorted(a)
    index = 0
    majority_counter = 0
    while index < right:
        if index + 1 < right and sorted_a[index] == sorted_a[index + 1]:
            majority_counter += 1
        elif majority_counter >= right // 2:
            return 1
        else:
            majority_counter = 0
        index += 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #data = [5, 2, 3, 9, 1, 2]
    #data = [11, 1, 1, 1, 1, 1,1 ,1, 1,3,4,5]
    #n = data[0]
    #a = data[1: n + 1]
    #print(data)
    print(get_majority_element(a,0, n))
    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)
