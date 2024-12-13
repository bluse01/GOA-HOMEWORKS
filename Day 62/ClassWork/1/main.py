def filter_array(arr1, arr2):
    result_arr = []
    for i, j in arr1, arr2:
        if i not in arr1:
            result_arr.append(i)
        if j not in arr2:
            result_arr.append(j)
                
    return result_arr

print(filter_array([2, 6, 4, 3, 5], [3, 6, 7, 8, 5, 9]))