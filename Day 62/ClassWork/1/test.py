def cut_array(arr1, arr2):
    result_arr = []
    for i in arr1:
        if i not in arr2:
            result_arr.append(i)
            
    arr1[:] = result_arr              
    print(arr1)

cut_array([2, 3, 5, 7, 8,], [2, 7, 3])