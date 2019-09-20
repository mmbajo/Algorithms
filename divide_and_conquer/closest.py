#Uses python3
import sys
import random
import math
inf = float('inf')

        
def merge_sort(A, idx = 0):
    n = len(A)
    if n <= 1:
        return A
    m = n//2
    B= merge_sort(A[0:m])
    C = merge_sort(A[m:n])
    A_prime = merge(B, C, idx = idx)
    return A_prime

def merge(B, C, idx = 0):
    #mid = len(B)
    D = []
    i = 0
    j = 0
    while i < len(B) and j < len(C):
        if B[i][idx] <= C[j][idx]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])

            j += 1
            
    if B is not None:
        D.extend(B[i:])
    if D is not None:
        D.extend(C[j:])
    return D
# prepare array X_ordered and Y_ordered

def sort_in_pairs(x, y):
    one_array = list(zip(x, y))
    #X_ordered = merge_sort(one_array, idx = 0)
    #Y_ordered = merge_sort(one_array, idx = 1)

    X_ordered = sorted(one_array, key = lambda x: x[0])
    Y_ordered = sorted(one_array, key = lambda x: x[1])

    return X_ordered, Y_ordered

def euclidian_distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])*(point1[0]-point2[0]) + (point1[1]-point2[1])*(point1[1]-point2[1]))

# def find_min_in_boundaries(y_sorted, sorted_array, m, d_min):
#     pivot = sorted_array[m][0]
#     Y_ordered = [i for i in y_sorted if pivot - d_min <= i[0] <= pivot + d_min]
#     n = len(Y_ordered)

#     for i in range(n - 1):
#         for j in range(i + 1, min(i + 8, n)):
#                 if abs(Y_ordered[i][1] - Y_ordered[j][1]) <=  d_min:
#                     d2 = euclidian_distance(Y_ordered[i], Y_ordered[j])
#                     if d2 < d_min:
#                         d_min = d2
#     return d_min
def find_min_in_boundaries(y_sorted, sorted_array, m, d_min):
    ln = len(sorted_array)
    pivot = sorted_array[m][0]
    
    left = sorted_array[0:m]
    bound_l = []
    for i in range(m):
        if abs(left[-1 - i][0] - pivot) <= d_min:
            bound_l.append(left[-1 - i])
        else:
            break
            
    right = sorted_array[m:ln]
    bound_r = []
    for i in range(ln-m):
        if abs(right[i][0] - pivot) <= d_min:
            bound_l.append(right[i])
        else:
            break
            
    bound = set(bound_l + bound_r)
    Y_ordered = [i for i in y_sorted if i in bound]
    n = len(Y_ordered)

    for i in range(n - 1):
        for j in range(i + 1, min(i + 8, n)):
                if abs(Y_ordered[i][1] - Y_ordered[j][1]) <=  d_min:
                #      break
                # else:
                    d2 = euclidian_distance(Y_ordered[i], Y_ordered[j])
                    if d2 < d_min:
                        d_min = d2
    return d_min
    
def minimum_distance_inner(y_sorted, sorted_array):
    n = len(sorted_array)
    if n <= 3:
        for i in range(n-1):
            for j in range(i + 1, n):
                df = min(euclidian_distance(sorted_array[i],sorted_array[j]), inf)
        return df
    
    
    m = n//2

    y_l = []
    y_r = []
    set_x_l = set(sorted_array[0:m])
    #set_x_r = set(sorted_array[m:n])
    #set_y = set(y_sorted)
    #y_l = list(set_y - set_x_r)
    #y_r = list(set_y - set_x_l)

    for x in y_sorted:
        if x in set_x_l:
            y_l.append(x)
        else:
            y_r.append(x)

    d1 = minimum_distance_inner(y_l, sorted_array[0:m])
    d2 = minimum_distance_inner(y_r, sorted_array[m:n])
    
    d = min(d1, d2)
    
    df = find_min_in_boundaries(y_sorted, sorted_array, m, d)
    
    
    return df

def minimum_distance(x, y):
    sorted_array, y_sorted = sort_in_pairs(x,y)
    return minimum_distance_inner(y_sorted, sorted_array)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x,y)))
