
def matrix_swap(m):
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            m[i], m[j] = m[j], m[i]
        
    print(m)

matrix = [ [1, 3],[1, 4], [4, 1],[2, 2] , [5, 3],[10, 2] ]
matrix_swap(matrix)