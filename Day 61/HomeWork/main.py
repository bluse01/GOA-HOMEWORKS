def filter_array(arr):
    for i in arr:
        for j in arr:
            if i == j:
                arr.remove(i)
                arr.remove(j)
                
    return arr
                

print(filter_array([5, 4, 5, "hello", "hello"]))