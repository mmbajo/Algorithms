# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    cache_array = [0, 1]
    for i in range(2, n+1):
        temp = cache_array[i-1] + cache_array[i-2] 
        cache_array.append(temp)
    return cache_array[n]

n = int(input())
print(calc_fib_fast(n))
