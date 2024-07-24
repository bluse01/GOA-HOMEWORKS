
def sort_a_list(lst):

    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] >= lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst     

my_list = [3, 1, 9, 5, 7, 4 ,6 , 8 , 2]

print(f"unsorted list: {my_list}")

sorted_list = sort_a_list(my_list)
print(f"sorted list: {sorted_list}")