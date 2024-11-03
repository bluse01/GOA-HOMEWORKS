
def mt(n):
    op = lambda a, b: a * b
    table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    new_arr = []
    for i in n:
        temp_arr = []
        for j in table:
            temp_arr.append(op(i, j))
        new_arr.append(temp_arr)
            
    return new_arr
    

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mt(nums))