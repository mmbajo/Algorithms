# Uses python3
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    weights = np.array(weights)
    values = np.array(values)
    ratio = values/ weights
    idx_for_sort = np.argsort(-ratio)
    weights = weights[idx_for_sort]
    values = values[idx_for_sort]
    ratio = ratio[idx_for_sort]
    total_value = 0
    for i in range(weights.shape[0]):
        if capacity == 0:
            return total_value
        to_take = ratio[i]
        to_take_weight = weights[i]
        while to_take_weight != 0 and capacity != 0:
            a = min(weights[i], capacity)
            total_value += a * ratio[i]
            to_take_weight -= a
            capacity -= a 
    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
