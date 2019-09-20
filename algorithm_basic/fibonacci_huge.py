# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_faster(n, m):
    if n <= 1:
        return n
    cache1 = {0: 0,
              1: 1}
    
    previous = 0
    current  = 1

#     for i in range(2, n+1):
#         print(i)
#         previous, current = current, previous + current
#         cache1[i] = current
#         if previous % m == 0 and current % m == 1:
#             break
    i = 2
    while True:
        previous, current = current, previous + current
        cache1[i] = current
        if previous % m == 0 and current % m == 1:
            break
        i+=1
    return cache1[n % (i-1)] % m



if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_faster(n, m))
