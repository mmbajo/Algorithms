#Uses python3

import sys

def isGreaterOrEqual(in_a, maxDigit):
    return int(in_a+maxDigit) >=  int(maxDigit+in_a)
            

def largest_number(a):
    #write your code here
    res = ""
    while len(a) != 0: 
        j = 0
        maxDigit = '0'
        for i in range(len(a)):
            if isGreaterOrEqual(a[i], maxDigit):
                maxDigit = a[i]
                j = i
        res += maxDigit
        del a[j]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
