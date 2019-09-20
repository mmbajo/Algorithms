# Uses python3
import sys
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

def binary_search_lefts(array, low, high, to_find):
    if high <= low:
        return low
    midpoint = low + (high - low)//2
#     if array[midpoint] == to_find:
#         return midpoint + 1
    if array[midpoint] > to_find:
        return binary_search_lefts(array, low, midpoint, to_find)
    else:
        return binary_search_lefts(array, midpoint+1, high, to_find)

def binary_search_rights(array, low, high, to_find):
    if high <= low:
        return low
    midpoint = (high - (high - low)//2) - 1
    #if array[midpoint] == to_find:
     #   return midpoint
    if array[midpoint] >= to_find:
        return binary_search_rights(array, low, midpoint, to_find)
    else:
        return binary_search_rights(array, midpoint+1, high, to_find)

def fast_count_segments(starts, ends, points):
    n_segments = len(starts)
    cnt = [0] * len(points)
    starts_temp = starts
    ends_temp = ends
    randomized_quicksort(starts_temp, 0, len(starts) - 1)
    randomized_quicksort(ends_temp, 0, len(starts) - 1)
    for i in range(len(points)):
        p = points[i]
        l = binary_search_lefts(starts, 0, n_segments, p)
        #print(l)
        r = n_segments - binary_search_rights(ends, 0, n_segments, p)
        #print(r)
        cnt[i] = l + r - n_segments
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
