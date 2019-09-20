# Uses python3
import sys
def merge(a, b, left, ave, right):
    num_inversion = 0
    i = left
    j = right
    k = ave

    counter = left
    while i <= ave and k <= j:
        if a[i] <= a[k]:
            b[counter] = a[i]
            i += 1
            counter += 1
        else:
            b[counter] = a[k]
            num_inversion += ave - i
            k += 1
            counter += 1
    while i <= ave:
        b[counter] = a[i]
        i += 1
        counter += 1
    while k <= j:
        b[counter] = a[k]
        k += 1
        counter += 1

    return num_inversion

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge(b, a, left, ave, right)

def merge_sort(A):
    n = len(A)
    if n <= 1:
        return A, 0
    m = n//2
    B, inv1 = merge_sort(A[0:m])
    C, inv2 = merge_sort(A[m:n])
    A_prime, inv3 = merge(B, C)
    return A_prime, inv1 + inv2 + inv3

def merge(B, C):
    mid = len(B)
    D = []
    inv = 0
    i = 0
    j = 0
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            inv += mid - i
            j += 1
            
    if B is not None:
        D.extend(B[i:])
    if D is not None:
        D.extend(C[j:])
    return D, inv

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #b = n * [0]
    b = a
    #print(get_number_of_inversions(a, b, 0, len(a)))
    print(merge_sort(a)[1])
