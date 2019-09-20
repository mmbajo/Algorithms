# Uses python3
import sys

def binary_search(array, low, high, to_find):
    if high <= low:
        return -1
    midpoint = low + (high - low)//2
    if array[midpoint] == to_find:
        return midpoint
    elif array[midpoint] > to_find:
        return binary_search(array, low, midpoint, to_find)
    else:
        return binary_search(array, midpoint+1, high, to_find)

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
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, 0, len(a), x), end = ' ')
