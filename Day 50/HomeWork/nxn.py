
def calc(m):
    res = []
    for i in m:
        if len(i) == 3:
            x, y, z = i
            res.append([x + y + z])
        
    return res

mat = [
    [2,4,5],
    [3,4,6],
    [1,2,8]
]

print(calc(mat))