
def more(n):
    op = lambda a, b: a + b
    
    new_arr = []
    for x, y in n:
        if op(x, y) >= 3:
            new_arr.append((x,y))
            
    return ", ".join(str(item) for item in new_arr)

nums = [(1,2), (2,3), (1,1), (0,1)]
print(more(nums))