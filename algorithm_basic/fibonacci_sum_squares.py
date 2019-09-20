# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10
def fibonacci_partial_sum_fast(m, n):
    if n <= 1:
        return n
    cache = {0: 0,
             1: 1}
    previous = 0
    current  = 1
    sum      = 1

    for i in range(2, 61):
        previous, current = current, previous + current
        sum += current
        cache[i] = sum
    
    to_return = ((n//60) * cache[60] + cache[n % 60]) - (((m-1)//60) * cache[60] + cache[(m-1) % 60])

    return to_return % 10
def fibonacci_sum_squares_fast(n):

    l1 = fibonacci_partial_sum_fast(n, n) % 10
    l2 = fibonacci_partial_sum_fast(n-1, n) % 10
    return (l1*l2) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_fast(n))
