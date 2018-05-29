# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.

    map_value_per_unit = {}
    for index, weight in enumerate(weights):
        value_per_unit = values[index] / weight
        map_value_per_unit[index] = value_per_unit

    sorted_max_value_per_unit = sorted(map_value_per_unit.items(), key=lambda value: value[1], reverse=True)

    for item in sorted_max_value_per_unit:
        index = item[0]
        if capacity == 0:
            return value
        else:
            weight = capacity if weights[index] > capacity else weights[index]
            value += weight * item[1]
            capacity = capacity - weight
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
