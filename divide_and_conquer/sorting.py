# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l;
    t = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
        if a[i] == x:
            j += 1
            t = j
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return t, j

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    t, m = partition3(a, l, r)
    randomized_quick_sort(a, l, t - 1);
    randomized_quick_sort(a, m + 1, r);


import random
def djkistra_3(A, p, r):
    x = A[p]
    lt = p
    gt = r
    i = p
    while i <= gt:
        if A[i] < x:
            A[i], A[lt] = A[lt], A[i]
            lt += 1
            i += 1
        elif A[i] > x:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
    return lt, gt
def partition3(A, p, r):
    x = A[r]
    i = p-1
    t = -1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[j], A[i] = A[i], A[j]
        elif A[j] == x:
            i += 1
            t = i
            A[j], A[i] = A[i], A[j]
    A[r], A[i + 1] = A[i + 1], A[r]
    if t == -1:
        t = i + 1
    return t, i + 1

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
            
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return djkistra_3(A, p, r)

def randomized_quicksort(A, p, r):
    if p < r:
        #t, q = randomized_partition(A, p, r)
        t, q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, t-1)
        randomized_quicksort(A, q+1, r)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quicksort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
