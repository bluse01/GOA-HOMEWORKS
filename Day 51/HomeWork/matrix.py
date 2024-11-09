
def calc(m):
    res1 = []
    res2 = []
    for i in range(len(m)):
        sum1 = 0
        sum2 = 0
        for j in range(0, len(m[i])):
            sum1 += m[i][j]
            sum2 += m[j][i]
             
        res1.append(sum1)
        res2.append(sum2)
        
    return res1, res2
            

matrix = [
    [2, 4, 5],
    [3, 8, 9],
    [1, 3, 2]
]

print(calc(matrix))