def sort_array(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
    return arr  

print(sort_array([2, 3, 7, 1, 9, 8, 5]))