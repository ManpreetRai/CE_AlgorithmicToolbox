# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


# knapsack without repetitions
def without_rep(W, w, n):
    value = [[0 for x in range(W + 1)] for y in range(n + 1)]

    for i in range(1, n + 1):
        for w_main in range(1, W + 1):
            value[i][w_main] = value[i - 1][w_main]

            if w[i - 1] <= w_main:
                val = value[i - 1][w_main - w[i - 1]] + w[i - 1]

                if value[i][w_main] < val:
                    value[i][w_main] = val

    return value[n][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))

    # #data = [10, 3, 1, 5, 8]
    # #data = [10, 4, 6, 3, 4, 2]
    # data = [2, 1, 1]
    # W = data[0]
    # n = data[1]
    # w = data[2:]
    # print(optimal_weight(W, w))
    print(without_rep(W, w, n))
