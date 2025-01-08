def manual_count(array, index):
    count = 0
    for i in array:
        if i == index:
            count += 1
            
    return count

def filter_array(arr):
    result_array = []
    for i in arr:
        if manual_count(arr, i) == 1:
            result_array.append(i)
                
    return result_array

print(filter_array([1, 2.2, 1, "h", "h", 3]))