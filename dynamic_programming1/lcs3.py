#Uses python3

import sys

def edit_distance_threelongsub(word1, word2, word3):
    x = len(word1)
    y = len(word2)
    z = len(word3)
    distance_matrix = [[[0 for i in range(x+1)] for j in range(y+1)] for k in range(z+1)]
    
    for i in range(x + 1):
        distance_matrix[0][0][i] = 0
    
    for j in range(y + 1):
        distance_matrix[0][j][0] = 0
    
    for k in range(z + 1):
        distance_matrix[k][0][0] = 0
        
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            for k in range(1, z + 1):
                if word1[i - 1] == word2[j-1] and word1[i - 1] == word3[k - 1]:
                    distance_matrix[k][j][i] = max(distance_matrix[k-1][j][i], distance_matrix[k][j-1][i], distance_matrix[k-1][j-1][i],
                                                   distance_matrix[k-1][j][i-1], distance_matrix[k][j-1][i-1], distance_matrix[k-1][j-1][i-1] + 1,
                                                   distance_matrix[k][j][i-1]) 
                else:
                    distance_matrix[k][j][i] = max(distance_matrix[k-1][j][i], distance_matrix[k][j-1][i], distance_matrix[k-1][j-1][i],
                                                   distance_matrix[k-1][j][i-1], distance_matrix[k][j-1][i-1], distance_matrix[k-1][j-1][i-1],
                                                   distance_matrix[k][j][i-1] ) 
    
    return distance_matrix[-1][-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(edit_distance_threelongsub(a, b, c))
