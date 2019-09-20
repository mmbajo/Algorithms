# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

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

def lcm(num1, num2):
    return num1*num2//gcd(num1, num2)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

