# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_fast(n):
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
    
    to_return = (n//60) * cache[60] + cache[n % 60]

    return to_return % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
