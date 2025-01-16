def matrix2d(rows, cols):
    res_array = []
    counter = 1
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(counter)
            counter += 1
        res_array.append(row)
    return res_array
print(matrix2d(2, 2))