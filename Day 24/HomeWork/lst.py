
def lst_configure(lst):
    for pos, i in enumerate(lst):
        if (i % 2) == 0:
            lst[pos] = i * i
        else:
            lst[pos] = i * 2
            
    return lst

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lst_configure(my_list))