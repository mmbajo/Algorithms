#Uses python3

import sys
import numpy as np

def max_dot_product(a, b):
    #write your code here
    a = np.sort(a)
    b = np.sort(b)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
