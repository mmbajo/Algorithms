# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def min_operations(n):
    '''
    n - number to be disected in to parts resulted from //2 //3 +1
    '''
    all_parent = [1] + [0] * n # an array for parents of its own index for which the min operation was attained
    all_min_operations = [0] * (n+1) # an array for minimum operation for the said index

    for k in range(1, n + 1):
        current_parent = k - 1
        current_minimum_operation = all_min_operations[current_parent] + 1

        if k % 3 == 0:
            parent = k//3
            num_operation = all_min_operations[parent] + 1
            if num_operation < current_minimum_operation:
                current_minimum_operation, current_parent = num_operation, parent
        
        if k % 2 == 0:
            parent = k//2
            num_operation = all_min_operations[parent] + 1
            if num_operation < current_minimum_operation:
                current_minimum_operation, current_parent = num_operation, parent
        
        all_parent[k], all_min_operations[k] = current_parent, current_minimum_operation

    numbers = []
    k = n
    while k > 0:
        numbers.append(k)
        k = all_parent[k]
    return list(reversed(numbers))
 


input = sys.stdin.read()
n = int(input)
sequence = list(min_operations(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
