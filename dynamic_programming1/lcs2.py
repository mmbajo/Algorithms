#Uses python3

import sys

def edit_distance_twolongsub(word1, word2):
    n = len(word1)
    m = len(word2)
    distance_matrix = [[0 for i in range(n+1)] for j in range(m+1)]
    
    for i in range(n + 1):
        distance_matrix[0][i] = 0
    
    for j in range(m + 1):
        distance_matrix[j][0] = 0
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j-1]:
                distance_matrix[j][i] = max(distance_matrix[j-1][i], distance_matrix[j][i-1], distance_matrix[j-1][i-1] + 1) 
            if word1[i - 1] != word2[j-1]:
                distance_matrix[j][i] = max(distance_matrix[j-1][i], distance_matrix[j][i-1], distance_matrix[j-1][i-1]) 
    
    return distance_matrix[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(edit_distance_twolongsub(a, b))
