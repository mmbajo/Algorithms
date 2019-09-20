# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(num1, num2):
    if num1 > num2:
        a = num2
        b = num1
    else:
        a = num1
        b = num2
    if a == 0:
        return b
    c = b % a
    return gcd(a,c)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
