# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))